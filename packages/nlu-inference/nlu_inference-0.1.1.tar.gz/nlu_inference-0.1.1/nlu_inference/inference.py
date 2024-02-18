from typing import Any, List, Tuple, Literal
from onnxruntime import InferenceSession, SessionOptions
from fasttext import load_model
from pathlib import Path
from .utils import ner_post_process
import json
import numpy as np
from .tokenizer import Tokenizer
from pydantic import validate_arguments



class FasttextInference():
    def __init__(self, model_path: str):
        super().__init__()
        if isinstance(model_path, str):
            self.model = load_model(model_path)
        if isinstance(model_path, Path):
            self.model = load_model(str(model_path))
    
    def __call__(self, query: str) -> Tuple[str, float]:
        """fasttext 模型推理

        Args:
            query (str): 原始问题文本
        """
        query = ' '.join(list(query))
        result = self.model.predict(query)
        label = result[0][0]
        score = result[1][0]
        return label, round(score, 4)
    
    
class NERInferenceLocal():
    """ner模型推理, 返回格式如下 (2, 6, '明天上午', 'DateChanged')
    """
    def __init__(self, 
                 embedding_model_path: str,
                 classifier_model_path: str,
                 tokenizer: Tokenizer,
                 label_path: str):
        super().__init__()
        so = SessionOptions()
        so.log_severity_level = 3
        if isinstance(classifier_model_path, str):
            self.classifier_model = InferenceSession(classifier_model_path, so)
        if isinstance(embedding_model_path, Path):
            self.classifier_model = InferenceSession(str(classifier_model_path), so)
        
        self.tokenizer = tokenizer
        
        with open(label_path, 'r') as f:
            self.id2label = json.load(f)
            
        self.embedding_model = InferenceSession(embedding_model_path, so)
    
    def __call__(self, query: str) -> List[Tuple[int, int, str, str]]:
        """ner 模型推理

        Args:
            query (str): 原始问题文本
        """
        tokens = self.tokenizer(query, padding=True)[0]
        embeddings = self.get_embeddings(ids=tokens.ids)
        labels = self.get_labels(embeddings)
        
        # 后处理
        ents = ner_post_process(labels, tokens=tokens)
        return ents
    
    
    def get_embeddings(self, ids: List[int]) -> np.ndarray:
        """获取embedding

        Args:
            query (str): 原始问题文本
        """
        input_ids = np.array(ids, dtype=np.int64).reshape(1, -1)
        # 获取embedding
        embeddings = self.embedding_model.run(None, {'input': input_ids})[0]
        embeddings = np.array(embeddings, dtype=np.float32)
        return embeddings
    
    
    def get_labels(self, embeddings: np.ndarray) -> List[str]:
        """获取标签

        Args:
            embeddings (np.ndarray): embedding
        """
        label_ids = self.classifier_model.run(None, {'input': embeddings})[0][0]
        # 兼容tf版本转换的onnx模型
        if len(label_ids.shape) == 2:
            label_ids = np.argmax(label_ids, axis=-1)
            
        labels = [self.id2label[str(i)] for i in label_ids]
        return labels
    
    
    
class NERInferenceCloud():
    """ner模型推理, 返回格式如下 (2, 6, '明天上午', 'DateChanged')
    """
    def __init__(self, 
                 model_path: str,
                 tokenizer: Tokenizer,
                 label_path: str):
        super().__init__()
        
        so = SessionOptions()
        so.log_severity_level = 3
        
        self.model = InferenceSession(str(model_path), so)
        
        self.tokenizer = tokenizer
        
        with open(label_path, 'r') as f:
            self.id2label = json.load(f)
    
    
    @validate_arguments
    def __call__(self, query: str) -> List[Tuple[int, int, str, str]]:
        """ner 模型推理

        Args:
            query (str): 原始问题文本
        """
        tokens = self.tokenizer([query], padding=True)[0]
        
        label_ids = self.model.run(None, {'input': np.array([tokens.ids], dtype=np.int64)})[0][0]
        # 兼容tf版本转换的onnx模型
        if len(label_ids.shape) == 2:
            label_ids = np.argmax(label_ids, axis=-1)
            
        labels = [self.id2label[str(i)] for i in label_ids]
        
        # 后处理
        ents = ner_post_process(labels, tokens=tokens)
        
        return ents