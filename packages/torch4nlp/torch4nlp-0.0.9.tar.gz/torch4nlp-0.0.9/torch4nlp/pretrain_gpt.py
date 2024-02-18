import os
import pdb
import copy
import logging
from argparse import ArgumentParser
import torch
from torch.utils.data import TensorDataset, DataLoader, RandomSampler
import transformers
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from torch4nlp import read_jsonl, read_txt


logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(filename)s - %(message)s')
logging.info('transformers version: {}'.format(transformers.__version__))


def load_examples_from_files(file_list):
    examples = []
    for file_path in file_list:
        for x in read_txt(file_path):
            examples.append(x)
    return examples


def build_dataloader(file_list, tokenizer, batch_size, max_len=1024):
    examples = load_examples_from_files(file_list)
    logging.info('tokenizing train data...')
    
    block_size = 4096
    
    # batch encoding
    total_ids = []
    i = 0
    while i < len(examples):
        batch_examples = examples[i:i + block_size]
        for ids in tokenizer(batch_examples)['input_ids']:
            total_ids += ids
        i += block_size

    # group text
    input_ids = []
    i = 0
    while i + max_len <= len(total_ids):
        input_ids.append(total_ids[i: i + max_len])
        i += max_len
    
    # build dataloader
    dataset = TensorDataset(torch.LongTensor(input_ids[:-1]))  # drop the last one
    sampler = RandomSampler(dataset)
    return DataLoader(dataset, sampler=sampler, batch_size=batch_size)
    

def get_arguments():
    parser = ArgumentParser()
    parser.add_argument('--plm_dir', type=str, default='model_hub/gpt2-xl')
    parser.add_argument('--batch_size', type=int, default=2)
    parser.add_argument('--train_epochs', type=int, default=1)
    parser.add_argument('--lr', type=float, default=1e-4)
    parser.add_argument('--max_len', type=int, default=512)
    parser.add_argument('--gradient_accumulation_step', type=int, default=64)
    parser.add_argument('--display_steps', type=int, default=10)
    parser.add_argument('--dump_steps', type=int, default=1000)
    args = parser.parse_args()
    return args
    
    
def main():
    args = get_arguments()
    tokenizer = GPT2TokenizerFast.from_pretrained(args.plm_dir)
    model = GPT2LMHeadModel.from_pretrained(args.plm_dir).to('cuda')
    dataloader = build_dataloader(
        [r'C:\Users\owen\Documents\Projects\torch4nlp\torch4nlp\中国通史.txt'], 
        tokenizer,
        args.batch_size,
        args.max_len
    )
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr)
    logging.info('start to train...')
    total_steps = args.train_epochs * len(dataloader) // (args.batch_size * args.gradient_accumulation_step)
    global_step = 0
    global_batch = 0
    optimizer.zero_grad()
    for epoch in range(args.train_epochs):
        model.train()
        for batch in dataloader:
            global_batch += 1
            
            input_ids = batch[0].to('cuda')
            labels = copy.deepcopy(input_ids)
            output = model(
                input_ids=input_ids, 
                labels=labels
            )
            loss = output.loss
            loss = loss / args.gradient_accumulation_step
            loss.backward()
            
            if global_batch % args.gradient_accumulation_step == 0:
                optimizer.step()
                optimizer.zero_grad()
                global_step += 1
                
            if global_batch % (args.gradient_accumulation_step * args.display_steps) == 0:
                logging.info('epoch: {}, global step: {}/{}, loss: {:.6f}'.format(epoch, global_step, total_steps, loss.item()))
    
            if global_batch % (args.gradient_accumulation_step * args.dump_steps) == 0:
                checkpoint_dir = 'gpt2-xl-cp-global-step-{}'.format(global_step)
                model.save_pretrained(checkpoint_dir)
                tokenizer.save_pretrained(checkpoint_dir)
                logging.info('checkpoint {} dumped'.format(checkpoint_dir))

    checkpoint_dir = 'gpt2-xl-cp-global-step-{}'.format(global_step)
    model.save_pretrained(checkpoint_dir)
    tokenizer.save_pretrained(checkpoint_dir)
    logging.info('checkpoint {} dumped'.format(checkpoint_dir))
    
        
if __name__ == '__main__':
    main()
    exit(0)
    """
    python pretrain_gpt.py --plm_dir model_hub/gpt2-xl --lr 1e-4 --batch_size 2 --train_epochs 1 --max_len 512 --gradient_accumulation_step 64 --display_steps 10 --dump_steps 1000
    """

    ds = load_dataset(
        "text", 
        data_files={
            "train": '中国通史.txt',
            "validation": 'eval.txt'
        }
    )
    print('===> dataset loaded!')
    print('data sample:', ds["train"][10])


    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_fast=True)

    def tokenize_function(examples):
        return tokenizer(examples["text"])

    print('===> tokenizer built!')

    tokenized_datasets = ds.map(tokenize_function, batched=True, remove_columns=["text"])

    print('===> dataset tokenized!')
    print('sample:', tokenized_datasets["train"][1])

    block_size = 128
    def group_texts(examples):
        # Concatenate all texts.
        concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
        total_length = len(concatenated_examples[list(examples.keys())[0]])
        # We drop the small remainder, we could add padding if the model supported it instead of this drop, you can
            # customize this part to your needs.
        total_length = (total_length // block_size) * block_size
        # Split by chunks of max_len.
        result = {
            k: [t[i : i + block_size] for i in range(0, total_length, block_size)]
            for k, t in concatenated_examples.items()
        }
        result["labels"] = result["input_ids"].copy()
        return result


    lm_datasets = tokenized_datasets.map(
        group_texts,
        batched=True,
        batch_size=1000,
        # num_proc=4,
    )

    print('===> text grouped!')
    print(tokenizer.decode(lm_datasets["train"][1]["input_ids"]))


    model = AutoModelForCausalLM.from_pretrained(model_checkpoint)
    # pdb.set_trace()


    from transformers import Trainer, TrainingArguments

    model_name = model_checkpoint.split("/")[-1]
    training_args = TrainingArguments(
        dump_checkpoint,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        gradient_accumulation_steps=16,
        num_train_epochs=1.0,
        evaluation_strategy = "epoch",
        learning_rate=2e-5,
        weight_decay=0.01,
        push_to_hub=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=lm_datasets["train"],
        eval_dataset=lm_datasets["validation"],
    )

    trainer.train()

    import math
    eval_results = trainer.evaluate()
    print(f"Perplexity: {math.exp(eval_results['eval_loss']):.2f}")