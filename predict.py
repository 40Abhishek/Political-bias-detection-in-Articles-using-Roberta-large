import torch
from transformers import RobertaTokenizerFast, RobertaForSequenceClassification

MODEL_PATH = "roberta_articles_classifier"
ID2LABEL = {0: "Left", 1: "Center", 2: "Right"}
MAX_LEN, STRIDE = 512, 256

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = RobertaTokenizerFast.from_pretrained(MODEL_PATH)
model = RobertaForSequenceClassification.from_pretrained(MODEL_PATH).to(device)
model.eval()

def get_text():
    print("Enter article text (press ENTER twice to finish):\n")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines).strip()

def predict(text: str):
    enc = tokenizer(
        text,
        return_tensors="pt",
        max_length=MAX_LEN,
        truncation=True,
        padding="max_length",
        stride=STRIDE,
        return_overflowing_tokens=True,
    )

    with torch.no_grad():
        logits = model(
            input_ids=enc["input_ids"].to(device),
            attention_mask=enc["attention_mask"].to(device),
        ).logits

    avg_logits = logits.mean(dim=0)
    probs = torch.softmax(avg_logits, dim=-1).cpu().tolist()
    pred_id = int(torch.argmax(avg_logits))
    return pred_id, probs
'-*+=
def main():
    text = get_text()
    if not text:
        print("No input given.")
        return

    pred_id, probs = predict(text)
    label = ID2LABEL[pred_id]
    prob_str = ", ".join(f"{ID2LABEL[i]}: {probs[i]:.3f}" for i in range(len(probs)))

    print("\nPrediction:")
    print("Predicted bias:", label)
    print("Class probabilities:", prob_str)

if __name__ == "__main__":
    main()
