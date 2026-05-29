import torch


def main():
    scores = torch.tensor([0.2, 0.8, 0.5])
    score_column = torch.tensor([[0.2], [0.8], [0.5]])
    score_row = torch.tensor([[0.2, 0.8, 0.5]])

    print("scores:", scores)
    print("scores shape:", scores.shape)

    print("score_column:", score_column)
    print("score_column shape:", score_column.shape)

    print("score_row:", score_row)
    print("score_row shape:", score_row.shape)

    best_action = torch.argmax(scores)
    print("best_action:", best_action)


if __name__ == "__main__":
    main()