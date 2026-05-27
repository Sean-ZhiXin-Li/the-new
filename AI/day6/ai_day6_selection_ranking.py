import torch

def select_best_action(scores):
    best_action = torch.argmax(scores)
    return best_action.item()

def main():
    scores = torch.tensor([0.2, 0.8, 0.5])

    best_action = select_best_action(scores)

    print("scores: ", scores)
    print("Best action: ", best_action)


if __name__ == "__main__":
    main()