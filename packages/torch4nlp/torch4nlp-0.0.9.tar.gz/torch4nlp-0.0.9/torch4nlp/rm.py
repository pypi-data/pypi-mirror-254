# reward modeling
import json
from typing import List, Optional, Dict, Union
from utils.file_util import read_jsonl


class RMResponse:
    def __init__(
        self, 
        content: str = None, 
        rm_score: float = None, 
        helpful: Optional[float] = None, 
        truthful: Optional[float] = None, 
        saftefy: Optional[float] = None, 
        source: Optional[str] = None, 
        comment: Optional[str] = None
    ):
        self.content = content
        self.rm_score = rm_score
        self.helpful = helpful
        self.truthful = truthful
        self.safety = saftefy
        self.source = source
        self.comment = comment
    
    def to_dict(self) -> Dict[str, Union[str, float]]:
        return {
            'content': self.content,
            'helpful': self.helpful,
            'truthful': self.truthful,
            'safety': self.safety,
            'rm_score': self.rm_score,
            'source': self.source,
            'comment': self.comment
        }
    
    def __str__(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)


class RMDataItem:
    def __init__(
        self, 
        ann_time: Optional[str] = None,  # annotate time
        data_batch: Optional[str] = None,  # data batch
        data_type: Optional[str] = None,
        task_type: Optional[str] = None,  # task tree 
        question: Optional[str] = None,  # prompt in clean style, easy to read
        prompt_id: str = None,
        prompt: List[str] = None,  # rm model input, may contains prefix
        response: List[RMResponse] = None, 
        vote_label: str = None  # sort answer of response list
    ):
        self.batch = batch
        self.ann_time = ann_time
        self.data_type = data_type
        self.task_type = task_type
        self.question = question
        self.prompt_id = prompt_id
        self.prompt = prompt
        self.response = response
    
    def to_dict(self) -> Dict[str, Union[str, float]]:
        return {'session': {
            "batch": self.batch,
            "time": self.ann_time,
            "data_type": self.data_type,
            "task_type": self.task_type,
            "question": self.question,
            "prompt_id": self.prompt_id,
            "prompt": self.prompt,
            "response": self.response,
            "vote_label": self.vote_label
        }}

    def __str__(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)


class RMTask:
    def train(self):
        """perform training
        """
        return NotImplemented
    
    def test(self, infile, ansfile):
        """perform testing, return metric such as top1 rate, fullmark rate, pair acc
        
        args:
            infile: inference file
            ansfile: test file
        """

        for line in read_jsonl(ansfile):
            ...
            
    
def rm_eval(infile, ansfile):
    """
    评测rm, 计算top1比例/满分比例/pair acc
    args:
        infile: inference file
        ansfile: test file
    """

    for line in read_jsonl(ansfile):
        line['session']['vote_label'].split(',')[0].split('=')