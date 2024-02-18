import psutil
from typing import Callable, List, Tuple, Optional
from wasabi import msg
import time
from .tokenizer import TokenList


def get_cpu_memory(tag: str):
    """获取函数运行时的cpu内存

    Args:
        tag (str): 标签
    """
    def out_wrapper(fn: Callable):
        def wrapper(*args, **kwargs):
            p = psutil.Process()
            cpu_memory = p.memory_info().rss
            outputs = fn(*args, **kwargs)
            cpu_memory = p.memory_info().rss - cpu_memory
            msg.good(f"{tag} cpu memory: {cpu_memory / 1024 / 1024}MB")
            return outputs
        return wrapper
    return out_wrapper

def get_spent_time(tag: str):
    """获取函数运行时的时间

    Args:
        tag (str): 标签
    """
    def out_wrapper(fn: Callable):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            outputs = fn(*args, **kwargs)
            end_time = time.time()
            msg.good(f"{tag} spent time: {end_time - start_time}")
            return outputs
        return wrapper
    return out_wrapper



def get_ents(tags: List[str]) -> List[Tuple[int, int, str]]:
    """从序列标签中提取实体

    Args:
        tags (List[str]): 序列标签.

    Returns:
        List[Tuple[int, int, str]]: 实体列表.例如, [(2, 6, 'PER')]
    """
    entities = []
    entity = []
    for i, tag in enumerate(tags):
        if tag.startswith('B-'):
            if entity:
                entities.append(tuple(entity))
            entity = [i, i + 1, tag.split('-')[1]]
        elif tag.startswith('I-'):
            if entity:
                if entity[2] == tag.split('-')[1]:
                    entity[1] = i + 1
        else:
            if entity:
                entities.append(tuple(entity))
            entity = []
    if len(entity) == 3:
        entities.append(tuple(entity))
    return entities
        
    
def ner_post_process(labels: List[str], tokens: Optional[TokenList] = None) -> List[Tuple[int, int, str, str]]:
    """对ner模型预测的token标签进行后处理，得到最终的实体

    Args:
        labels (List[str]): 模型预测的序列标签.
        text (str): 原始文本.

    Returns:
        List[Tuple[int, int, str, str]]: 实体列表.例如, [(2, 6, '明天上午', 'DateChanged')]
    """
    if tokens:
        assert len(labels) == len(tokens)
    ents = get_ents(labels)
    if not tokens:
        return ents
    results = []
    for ent in ents:
        start, end, label = ent
        start_char = tokens.token_to_char(start)[0]
        end_char = tokens.token_to_char(end - 1)[-1] + 1
        results.append((start_char, end_char, tokens.processed_text[start_char:end_char], label))
    return results