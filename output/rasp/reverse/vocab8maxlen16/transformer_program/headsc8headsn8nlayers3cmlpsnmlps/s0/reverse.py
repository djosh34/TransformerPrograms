import numpy as np
import pandas as pd


def select_closest(keys, queries, predicate):
    scores = [[False for _ in keys] for _ in queries]
    for i, q in enumerate(queries):
        matches = [j for j, k in enumerate(keys) if predicate(q, k)]
        if not (any(matches)):
            scores[i][0] = True
        else:
            j = min(matches, key=lambda j: len(matches) if j == i else abs(i - j))
            scores[i][j] = True
    return scores


def select(keys, queries, predicate):
    return [[predicate(q, k) for k in keys] for q in queries]


def aggregate(attention, values):
    return [[v for a, v in zip(attn, values) if a][0] for attn in attention]


def aggregate_sum(attention, values):
    return [sum([v for a, v in zip(attn, values) if a]) for attn in attention]


def run(tokens):

    # classifier weights ##########################################
    classifier_weights = pd.read_csv(
        "output/rasp/reverse/vocab8maxlen16/transformer_program/headsc8headsn8nlayers3cmlpsnmlps/s0/reverse_weights.csv",
        index_col=[0, 1],
        dtype={"feature": str},
    )
    # inputs #####################################################
    token_scores = classifier_weights.loc[[("tokens", str(v)) for v in tokens]]

    positions = list(range(len(tokens)))
    position_scores = classifier_weights.loc[[("positions", str(v)) for v in positions]]

    ones = [1 for _ in range(len(tokens))]
    one_scores = classifier_weights.loc[[("ones", "_") for v in ones]].mul(ones, axis=0)

    # attn_0_0 ####################################################
    def predicate_0_0(q_position, k_position):
        if q_position in {0}:
            return k_position == 4
        elif q_position in {1}:
            return k_position == 6
        elif q_position in {2}:
            return k_position == 11
        elif q_position in {3}:
            return k_position == 12
        elif q_position in {10, 4, 5, 6}:
            return k_position == 15
        elif q_position in {7}:
            return k_position == 7
        elif q_position in {8, 11}:
            return k_position == 3
        elif q_position in {9}:
            return k_position == 5
        elif q_position in {12}:
            return k_position == 2
        elif q_position in {13, 14, 15}:
            return k_position == 1

    attn_0_0_pattern = select_closest(positions, positions, predicate_0_0)
    attn_0_0_outputs = aggregate(attn_0_0_pattern, tokens)
    attn_0_0_output_scores = classifier_weights.loc[
        [("attn_0_0_outputs", str(v)) for v in attn_0_0_outputs]
    ]

    # attn_0_1 ####################################################
    def predicate_0_1(q_position, k_position):
        if q_position in {0, 7}:
            return k_position == 4
        elif q_position in {1}:
            return k_position == 7
        elif q_position in {2}:
            return k_position == 8
        elif q_position in {3}:
            return k_position == 9
        elif q_position in {4}:
            return k_position == 10
        elif q_position in {10, 11, 5}:
            return k_position == 3
        elif q_position in {8, 9, 12, 6}:
            return k_position == 2
        elif q_position in {13, 14, 15}:
            return k_position == 1

    attn_0_1_pattern = select_closest(positions, positions, predicate_0_1)
    attn_0_1_outputs = aggregate(attn_0_1_pattern, tokens)
    attn_0_1_output_scores = classifier_weights.loc[
        [("attn_0_1_outputs", str(v)) for v in attn_0_1_outputs]
    ]

    # attn_0_2 ####################################################
    def predicate_0_2(q_position, k_position):
        if q_position in {0, 5, 6}:
            return k_position == 7
        elif q_position in {1}:
            return k_position == 13
        elif q_position in {2}:
            return k_position == 12
        elif q_position in {3}:
            return k_position == 11
        elif q_position in {4, 15}:
            return k_position == 9
        elif q_position in {7}:
            return k_position == 3
        elif q_position in {8}:
            return k_position == 6
        elif q_position in {9, 10}:
            return k_position == 4
        elif q_position in {11, 12, 13, 14}:
            return k_position == 1

    attn_0_2_pattern = select_closest(positions, positions, predicate_0_2)
    attn_0_2_outputs = aggregate(attn_0_2_pattern, tokens)
    attn_0_2_output_scores = classifier_weights.loc[
        [("attn_0_2_outputs", str(v)) for v in attn_0_2_outputs]
    ]

    # attn_0_3 ####################################################
    def predicate_0_3(q_position, k_position):
        if q_position in {0, 10}:
            return k_position == 5
        elif q_position in {1}:
            return k_position == 8
        elif q_position in {2, 3, 6}:
            return k_position == 9
        elif q_position in {4}:
            return k_position == 11
        elif q_position in {5}:
            return k_position == 10
        elif q_position in {15, 14, 7}:
            return k_position == 1
        elif q_position in {8}:
            return k_position == 7
        elif q_position in {9}:
            return k_position == 6
        elif q_position in {11}:
            return k_position == 4
        elif q_position in {12}:
            return k_position == 3
        elif q_position in {13}:
            return k_position == 2

    attn_0_3_pattern = select_closest(positions, positions, predicate_0_3)
    attn_0_3_outputs = aggregate(attn_0_3_pattern, tokens)
    attn_0_3_output_scores = classifier_weights.loc[
        [("attn_0_3_outputs", str(v)) for v in attn_0_3_outputs]
    ]

    # attn_0_4 ####################################################
    def predicate_0_4(q_position, k_position):
        if q_position in {0}:
            return k_position == 12
        elif q_position in {1}:
            return k_position == 9
        elif q_position in {2, 4}:
            return k_position == 7
        elif q_position in {3}:
            return k_position == 6
        elif q_position in {5, 8, 9, 10, 11, 12, 13}:
            return k_position == 15
        elif q_position in {6}:
            return k_position == 3
        elif q_position in {7}:
            return k_position == 8
        elif q_position in {14, 15}:
            return k_position == 1

    attn_0_4_pattern = select_closest(positions, positions, predicate_0_4)
    attn_0_4_outputs = aggregate(attn_0_4_pattern, tokens)
    attn_0_4_output_scores = classifier_weights.loc[
        [("attn_0_4_outputs", str(v)) for v in attn_0_4_outputs]
    ]

    # attn_0_5 ####################################################
    def predicate_0_5(position, token):
        if position in {0, 6}:
            return token == "0"
        elif position in {1, 2, 3, 4, 7}:
            return token == "4"
        elif position in {11, 5, 14}:
            return token == "2"
        elif position in {8, 10, 13}:
            return token == "</s>"
        elif position in {9, 15}:
            return token == "<s>"
        elif position in {12}:
            return token == "3"

    attn_0_5_pattern = select_closest(tokens, positions, predicate_0_5)
    attn_0_5_outputs = aggregate(attn_0_5_pattern, tokens)
    attn_0_5_output_scores = classifier_weights.loc[
        [("attn_0_5_outputs", str(v)) for v in attn_0_5_outputs]
    ]

    # attn_0_6 ####################################################
    def predicate_0_6(q_position, k_position):
        if q_position in {0, 9, 10, 11, 12}:
            return k_position == 1
        elif q_position in {8, 1, 2}:
            return k_position == 10
        elif q_position in {3, 6}:
            return k_position == 6
        elif q_position in {4, 5}:
            return k_position == 8
        elif q_position in {13, 7}:
            return k_position == 15
        elif q_position in {14}:
            return k_position == 14
        elif q_position in {15}:
            return k_position == 9

    attn_0_6_pattern = select_closest(positions, positions, predicate_0_6)
    attn_0_6_outputs = aggregate(attn_0_6_pattern, tokens)
    attn_0_6_output_scores = classifier_weights.loc[
        [("attn_0_6_outputs", str(v)) for v in attn_0_6_outputs]
    ]

    # attn_0_7 ####################################################
    def predicate_0_7(q_position, k_position):
        if q_position in {0, 5}:
            return k_position == 15
        elif q_position in {1}:
            return k_position == 14
        elif q_position in {2}:
            return k_position == 13
        elif q_position in {3}:
            return k_position == 12
        elif q_position in {4}:
            return k_position == 11
        elif q_position in {6}:
            return k_position == 9
        elif q_position in {7}:
            return k_position == 8
        elif q_position in {8}:
            return k_position == 7
        elif q_position in {9}:
            return k_position == 6
        elif q_position in {10}:
            return k_position == 5
        elif q_position in {11}:
            return k_position == 4
        elif q_position in {12}:
            return k_position == 0
        elif q_position in {13}:
            return k_position == 2
        elif q_position in {14, 15}:
            return k_position == 1

    attn_0_7_pattern = select_closest(positions, positions, predicate_0_7)
    attn_0_7_outputs = aggregate(attn_0_7_pattern, tokens)
    attn_0_7_output_scores = classifier_weights.loc[
        [("attn_0_7_outputs", str(v)) for v in attn_0_7_outputs]
    ]

    # num_attn_0_0 ####################################################
    def num_predicate_0_0(q_token, k_token):
        if q_token in {"2", "3", "0", "<s>", "4", "1"}:
            return k_token == ""
        elif q_token in {"</s>"}:
            return k_token == "<pad>"

    num_attn_0_0_pattern = select(tokens, tokens, num_predicate_0_0)
    num_attn_0_0_outputs = aggregate_sum(num_attn_0_0_pattern, ones)
    num_attn_0_0_output_scores = classifier_weights.loc[
        [("num_attn_0_0_outputs", "_") for v in num_attn_0_0_outputs]
    ].mul(num_attn_0_0_outputs, axis=0)

    # num_attn_0_1 ####################################################
    def num_predicate_0_1(token, position):
        if token in {"2", "4", "0"}:
            return position == 9
        elif token in {"1"}:
            return position == 6
        elif token in {"3"}:
            return position == 12
        elif token in {"<s>", "</s>"}:
            return position == 15

    num_attn_0_1_pattern = select(positions, tokens, num_predicate_0_1)
    num_attn_0_1_outputs = aggregate_sum(num_attn_0_1_pattern, ones)
    num_attn_0_1_output_scores = classifier_weights.loc[
        [("num_attn_0_1_outputs", "_") for v in num_attn_0_1_outputs]
    ].mul(num_attn_0_1_outputs, axis=0)

    # num_attn_0_2 ####################################################
    def num_predicate_0_2(q_position, k_position):
        if q_position in {0, 3, 5, 6, 8, 9, 10, 11}:
            return k_position == 15
        elif q_position in {1, 4}:
            return k_position == 0
        elif q_position in {2, 13}:
            return k_position == 7
        elif q_position in {15, 7}:
            return k_position == 11
        elif q_position in {12}:
            return k_position == 2
        elif q_position in {14}:
            return k_position == 13

    num_attn_0_2_pattern = select(positions, positions, num_predicate_0_2)
    num_attn_0_2_outputs = aggregate_sum(num_attn_0_2_pattern, ones)
    num_attn_0_2_output_scores = classifier_weights.loc[
        [("num_attn_0_2_outputs", "_") for v in num_attn_0_2_outputs]
    ].mul(num_attn_0_2_outputs, axis=0)

    # num_attn_0_3 ####################################################
    def num_predicate_0_3(token, position):
        if token in {"3", "0"}:
            return position == 8
        elif token in {"2", "1"}:
            return position == 9
        elif token in {"4"}:
            return position == 11
        elif token in {"</s>"}:
            return position == 15
        elif token in {"<s>"}:
            return position == 0

    num_attn_0_3_pattern = select(positions, tokens, num_predicate_0_3)
    num_attn_0_3_outputs = aggregate_sum(num_attn_0_3_pattern, ones)
    num_attn_0_3_output_scores = classifier_weights.loc[
        [("num_attn_0_3_outputs", "_") for v in num_attn_0_3_outputs]
    ].mul(num_attn_0_3_outputs, axis=0)

    # num_attn_0_4 ####################################################
    def num_predicate_0_4(token, position):
        if token in {"0"}:
            return position == 12
        elif token in {"1"}:
            return position == 7
        elif token in {"2", "3"}:
            return position == 9
        elif token in {"4"}:
            return position == 8
        elif token in {"<s>", "</s>"}:
            return position == 15

    num_attn_0_4_pattern = select(positions, tokens, num_predicate_0_4)
    num_attn_0_4_outputs = aggregate_sum(num_attn_0_4_pattern, ones)
    num_attn_0_4_output_scores = classifier_weights.loc[
        [("num_attn_0_4_outputs", "_") for v in num_attn_0_4_outputs]
    ].mul(num_attn_0_4_outputs, axis=0)

    # num_attn_0_5 ####################################################
    def num_predicate_0_5(token, position):
        if token in {"2", "3", "0", "1"}:
            return position == 14
        elif token in {"4"}:
            return position == 1
        elif token in {"<s>", "</s>"}:
            return position == 15

    num_attn_0_5_pattern = select(positions, tokens, num_predicate_0_5)
    num_attn_0_5_outputs = aggregate_sum(num_attn_0_5_pattern, ones)
    num_attn_0_5_output_scores = classifier_weights.loc[
        [("num_attn_0_5_outputs", "_") for v in num_attn_0_5_outputs]
    ].mul(num_attn_0_5_outputs, axis=0)

    # num_attn_0_6 ####################################################
    def num_predicate_0_6(token, position):
        if token in {"0"}:
            return position == 14
        elif token in {"1"}:
            return position == 0
        elif token in {"2", "3", "<s>", "</s>"}:
            return position == 15
        elif token in {"4"}:
            return position == 12

    num_attn_0_6_pattern = select(positions, tokens, num_predicate_0_6)
    num_attn_0_6_outputs = aggregate_sum(num_attn_0_6_pattern, ones)
    num_attn_0_6_output_scores = classifier_weights.loc[
        [("num_attn_0_6_outputs", "_") for v in num_attn_0_6_outputs]
    ].mul(num_attn_0_6_outputs, axis=0)

    # num_attn_0_7 ####################################################
    def num_predicate_0_7(token, position):
        if token in {"2", "0"}:
            return position == 9
        elif token in {"4", "1"}:
            return position == 12
        elif token in {"3"}:
            return position == 8
        elif token in {"<s>", "</s>"}:
            return position == 15

    num_attn_0_7_pattern = select(positions, tokens, num_predicate_0_7)
    num_attn_0_7_outputs = aggregate_sum(num_attn_0_7_pattern, ones)
    num_attn_0_7_output_scores = classifier_weights.loc[
        [("num_attn_0_7_outputs", "_") for v in num_attn_0_7_outputs]
    ].mul(num_attn_0_7_outputs, axis=0)

    # mlp_0_0 #####################################################
    def mlp_0_0(attn_0_3_output, attn_0_4_output):
        key = (attn_0_3_output, attn_0_4_output)
        if key in {
            ("0", "</s>"),
            ("2", "</s>"),
            ("3", "</s>"),
            ("4", "</s>"),
            ("</s>", "0"),
            ("</s>", "2"),
            ("</s>", "4"),
            ("</s>", "<s>"),
        }:
            return 12
        elif key in {("</s>", "3"), ("</s>", "</s>"), ("<s>", "</s>")}:
            return 14
        elif key in {("1", "</s>"), ("</s>", "1")}:
            return 5
        return 0

    mlp_0_0_outputs = [
        mlp_0_0(k0, k1) for k0, k1 in zip(attn_0_3_outputs, attn_0_4_outputs)
    ]
    mlp_0_0_output_scores = classifier_weights.loc[
        [("mlp_0_0_outputs", str(v)) for v in mlp_0_0_outputs]
    ]

    # mlp_0_1 #####################################################
    def mlp_0_1(attn_0_4_output, attn_0_3_output):
        key = (attn_0_4_output, attn_0_3_output)
        if key in {
            ("1", "</s>"),
            ("2", "</s>"),
            ("3", "</s>"),
            ("4", "</s>"),
            ("</s>", "1"),
            ("</s>", "2"),
            ("</s>", "3"),
            ("</s>", "4"),
            ("</s>", "</s>"),
            ("</s>", "<s>"),
            ("<s>", "</s>"),
        }:
            return 9
        elif key in {("</s>", "0")}:
            return 8
        elif key in {("0", "</s>")}:
            return 12
        return 2

    mlp_0_1_outputs = [
        mlp_0_1(k0, k1) for k0, k1 in zip(attn_0_4_outputs, attn_0_3_outputs)
    ]
    mlp_0_1_output_scores = classifier_weights.loc[
        [("mlp_0_1_outputs", str(v)) for v in mlp_0_1_outputs]
    ]

    # num_mlp_0_0 #################################################
    def num_mlp_0_0(num_attn_0_6_output, num_attn_0_0_output):
        key = (num_attn_0_6_output, num_attn_0_0_output)
        return 14

    num_mlp_0_0_outputs = [
        num_mlp_0_0(k0, k1)
        for k0, k1 in zip(num_attn_0_6_outputs, num_attn_0_0_outputs)
    ]
    num_mlp_0_0_output_scores = classifier_weights.loc[
        [("num_mlp_0_0_outputs", str(v)) for v in num_mlp_0_0_outputs]
    ]

    # num_mlp_0_1 #################################################
    def num_mlp_0_1(num_attn_0_5_output, num_attn_0_4_output):
        key = (num_attn_0_5_output, num_attn_0_4_output)
        if key in {
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
            (2, 4),
            (3, 1),
            (3, 2),
            (3, 3),
            (3, 4),
            (3, 5),
            (4, 1),
            (4, 2),
            (4, 3),
            (4, 4),
            (4, 5),
            (4, 6),
            (4, 7),
            (5, 2),
            (5, 3),
            (5, 4),
            (5, 5),
            (5, 6),
            (5, 7),
            (5, 8),
            (6, 3),
            (6, 4),
            (6, 5),
            (6, 6),
            (6, 7),
            (6, 8),
            (6, 9),
            (6, 10),
            (7, 4),
            (7, 5),
            (7, 6),
            (7, 7),
            (7, 8),
            (7, 9),
            (7, 10),
            (7, 11),
            (8, 5),
            (8, 6),
            (8, 7),
            (8, 8),
            (8, 9),
            (8, 10),
            (8, 11),
            (8, 12),
            (8, 13),
            (9, 5),
            (9, 6),
            (9, 7),
            (9, 8),
            (9, 9),
            (9, 10),
            (9, 11),
            (9, 12),
            (9, 13),
            (9, 14),
            (10, 6),
            (10, 7),
            (10, 8),
            (10, 9),
            (10, 10),
            (10, 11),
            (10, 12),
            (10, 13),
            (10, 14),
            (10, 15),
            (11, 7),
            (11, 8),
            (11, 9),
            (11, 10),
            (11, 11),
            (11, 12),
            (11, 13),
            (11, 14),
            (11, 15),
            (12, 8),
            (12, 9),
            (12, 10),
            (12, 11),
            (12, 12),
            (12, 13),
            (12, 14),
            (12, 15),
            (13, 9),
            (13, 10),
            (13, 11),
            (13, 12),
            (13, 13),
            (13, 14),
            (13, 15),
            (14, 9),
            (14, 10),
            (14, 11),
            (14, 12),
            (14, 13),
            (14, 14),
            (14, 15),
            (15, 10),
            (15, 11),
            (15, 12),
            (15, 13),
            (15, 14),
            (15, 15),
        }:
            return 6
        return 13

    num_mlp_0_1_outputs = [
        num_mlp_0_1(k0, k1)
        for k0, k1 in zip(num_attn_0_5_outputs, num_attn_0_4_outputs)
    ]
    num_mlp_0_1_output_scores = classifier_weights.loc[
        [("num_mlp_0_1_outputs", str(v)) for v in num_mlp_0_1_outputs]
    ]

    # attn_1_0 ####################################################
    def predicate_1_0(q_position, k_position):
        if q_position in {0, 1, 4}:
            return k_position == 8
        elif q_position in {2, 3}:
            return k_position == 6
        elif q_position in {5, 6}:
            return k_position == 9
        elif q_position in {7}:
            return k_position == 11
        elif q_position in {8, 9}:
            return k_position == 12
        elif q_position in {10, 11}:
            return k_position == 13
        elif q_position in {12}:
            return k_position == 14
        elif q_position in {13}:
            return k_position == 15
        elif q_position in {14}:
            return k_position == 3
        elif q_position in {15}:
            return k_position == 2

    attn_1_0_pattern = select_closest(positions, positions, predicate_1_0)
    attn_1_0_outputs = aggregate(attn_1_0_pattern, attn_0_1_outputs)
    attn_1_0_output_scores = classifier_weights.loc[
        [("attn_1_0_outputs", str(v)) for v in attn_1_0_outputs]
    ]

    # attn_1_1 ####################################################
    def predicate_1_1(q_position, k_position):
        if q_position in {0, 4, 5, 7}:
            return k_position == 6
        elif q_position in {1}:
            return k_position == 1
        elif q_position in {2}:
            return k_position == 3
        elif q_position in {3}:
            return k_position == 4
        elif q_position in {12, 6, 15}:
            return k_position == 15
        elif q_position in {8}:
            return k_position == 9
        elif q_position in {9}:
            return k_position == 10
        elif q_position in {10}:
            return k_position == 11
        elif q_position in {11, 13, 14}:
            return k_position == 12

    attn_1_1_pattern = select_closest(positions, positions, predicate_1_1)
    attn_1_1_outputs = aggregate(attn_1_1_pattern, attn_0_6_outputs)
    attn_1_1_output_scores = classifier_weights.loc[
        [("attn_1_1_outputs", str(v)) for v in attn_1_1_outputs]
    ]

    # attn_1_2 ####################################################
    def predicate_1_2(attn_0_0_output, mlp_0_1_output):
        if attn_0_0_output in {"0"}:
            return mlp_0_1_output == 12
        elif attn_0_0_output in {"3", "1"}:
            return mlp_0_1_output == 7
        elif attn_0_0_output in {"2"}:
            return mlp_0_1_output == 13
        elif attn_0_0_output in {"4"}:
            return mlp_0_1_output == 6
        elif attn_0_0_output in {"</s>"}:
            return mlp_0_1_output == 5
        elif attn_0_0_output in {"<s>"}:
            return mlp_0_1_output == 14

    attn_1_2_pattern = select_closest(mlp_0_1_outputs, attn_0_0_outputs, predicate_1_2)
    attn_1_2_outputs = aggregate(attn_1_2_pattern, tokens)
    attn_1_2_output_scores = classifier_weights.loc[
        [("attn_1_2_outputs", str(v)) for v in attn_1_2_outputs]
    ]

    # attn_1_3 ####################################################
    def predicate_1_3(position, token):
        if position in {0, 6, 15}:
            return token == ""
        elif position in {1, 9}:
            return token == "3"
        elif position in {2, 3, 4, 7, 10, 12, 13, 14}:
            return token == "</s>"
        elif position in {8, 11, 5}:
            return token == "<s>"

    attn_1_3_pattern = select_closest(tokens, positions, predicate_1_3)
    attn_1_3_outputs = aggregate(attn_1_3_pattern, attn_0_1_outputs)
    attn_1_3_output_scores = classifier_weights.loc[
        [("attn_1_3_outputs", str(v)) for v in attn_1_3_outputs]
    ]

    # attn_1_4 ####################################################
    def predicate_1_4(attn_0_4_output, position):
        if attn_0_4_output in {"4", "3", "0", "1"}:
            return position == 14
        elif attn_0_4_output in {"2"}:
            return position == 13
        elif attn_0_4_output in {"</s>"}:
            return position == 5
        elif attn_0_4_output in {"<s>"}:
            return position == 2

    attn_1_4_pattern = select_closest(positions, attn_0_4_outputs, predicate_1_4)
    attn_1_4_outputs = aggregate(attn_1_4_pattern, tokens)
    attn_1_4_output_scores = classifier_weights.loc[
        [("attn_1_4_outputs", str(v)) for v in attn_1_4_outputs]
    ]

    # attn_1_5 ####################################################
    def predicate_1_5(attn_0_7_output, token):
        if attn_0_7_output in {"4", "<s>", "0"}:
            return token == "1"
        elif attn_0_7_output in {"2", "3", "</s>", "1"}:
            return token == ""

    attn_1_5_pattern = select_closest(tokens, attn_0_7_outputs, predicate_1_5)
    attn_1_5_outputs = aggregate(attn_1_5_pattern, attn_0_3_outputs)
    attn_1_5_output_scores = classifier_weights.loc[
        [("attn_1_5_outputs", str(v)) for v in attn_1_5_outputs]
    ]

    # attn_1_6 ####################################################
    def predicate_1_6(attn_0_7_output, position):
        if attn_0_7_output in {"2", "3", "0", "1"}:
            return position == 13
        elif attn_0_7_output in {"4"}:
            return position == 12
        elif attn_0_7_output in {"</s>"}:
            return position == 10
        elif attn_0_7_output in {"<s>"}:
            return position == 11

    attn_1_6_pattern = select_closest(positions, attn_0_7_outputs, predicate_1_6)
    attn_1_6_outputs = aggregate(attn_1_6_pattern, attn_0_7_outputs)
    attn_1_6_output_scores = classifier_weights.loc[
        [("attn_1_6_outputs", str(v)) for v in attn_1_6_outputs]
    ]

    # attn_1_7 ####################################################
    def predicate_1_7(attn_0_7_output, position):
        if attn_0_7_output in {"4", "3", "0", "1"}:
            return position == 13
        elif attn_0_7_output in {"2"}:
            return position == 12
        elif attn_0_7_output in {"</s>"}:
            return position == 8
        elif attn_0_7_output in {"<s>"}:
            return position == 1

    attn_1_7_pattern = select_closest(positions, attn_0_7_outputs, predicate_1_7)
    attn_1_7_outputs = aggregate(attn_1_7_pattern, attn_0_2_outputs)
    attn_1_7_output_scores = classifier_weights.loc[
        [("attn_1_7_outputs", str(v)) for v in attn_1_7_outputs]
    ]

    # num_attn_1_0 ####################################################
    def num_predicate_1_0(attn_0_7_output, mlp_0_0_output):
        if attn_0_7_output in {"2", "3", "0"}:
            return mlp_0_0_output == 10
        elif attn_0_7_output in {"<s>", "</s>", "1"}:
            return mlp_0_0_output == 12
        elif attn_0_7_output in {"4"}:
            return mlp_0_0_output == 11

    num_attn_1_0_pattern = select(mlp_0_0_outputs, attn_0_7_outputs, num_predicate_1_0)
    num_attn_1_0_outputs = aggregate_sum(num_attn_1_0_pattern, num_attn_0_2_outputs)
    num_attn_1_0_output_scores = classifier_weights.loc[
        [("num_attn_1_0_outputs", "_") for v in num_attn_1_0_outputs]
    ].mul(num_attn_1_0_outputs, axis=0)

    # num_attn_1_1 ####################################################
    def num_predicate_1_1(attn_0_7_output, attn_0_4_output):
        if attn_0_7_output in {"2", "3", "0", "<s>", "</s>", "4"}:
            return attn_0_4_output == ""
        elif attn_0_7_output in {"1"}:
            return attn_0_4_output == "</s>"

    num_attn_1_1_pattern = select(attn_0_4_outputs, attn_0_7_outputs, num_predicate_1_1)
    num_attn_1_1_outputs = aggregate_sum(num_attn_1_1_pattern, num_attn_0_2_outputs)
    num_attn_1_1_output_scores = classifier_weights.loc[
        [("num_attn_1_1_outputs", "_") for v in num_attn_1_1_outputs]
    ].mul(num_attn_1_1_outputs, axis=0)

    # num_attn_1_2 ####################################################
    def num_predicate_1_2(attn_0_3_output, attn_0_0_output):
        if attn_0_3_output in {"</s>", "3", "0", "1"}:
            return attn_0_0_output == ""
        elif attn_0_3_output in {"2"}:
            return attn_0_0_output == "<pad>"
        elif attn_0_3_output in {"4"}:
            return attn_0_0_output == "</s>"
        elif attn_0_3_output in {"<s>"}:
            return attn_0_0_output == "<s>"

    num_attn_1_2_pattern = select(attn_0_0_outputs, attn_0_3_outputs, num_predicate_1_2)
    num_attn_1_2_outputs = aggregate_sum(num_attn_1_2_pattern, num_attn_0_5_outputs)
    num_attn_1_2_output_scores = classifier_weights.loc[
        [("num_attn_1_2_outputs", "_") for v in num_attn_1_2_outputs]
    ].mul(num_attn_1_2_outputs, axis=0)

    # num_attn_1_3 ####################################################
    def num_predicate_1_3(attn_0_7_output, attn_0_4_output):
        if attn_0_7_output in {"0"}:
            return attn_0_4_output == "</s>"
        elif attn_0_7_output in {"2", "3", "<s>", "</s>", "4", "1"}:
            return attn_0_4_output == ""

    num_attn_1_3_pattern = select(attn_0_4_outputs, attn_0_7_outputs, num_predicate_1_3)
    num_attn_1_3_outputs = aggregate_sum(num_attn_1_3_pattern, num_attn_0_2_outputs)
    num_attn_1_3_output_scores = classifier_weights.loc[
        [("num_attn_1_3_outputs", "_") for v in num_attn_1_3_outputs]
    ].mul(num_attn_1_3_outputs, axis=0)

    # num_attn_1_4 ####################################################
    def num_predicate_1_4(attn_0_1_output, position):
        if attn_0_1_output in {"2", "3", "0"}:
            return position == 0
        elif attn_0_1_output in {"1"}:
            return position == 15
        elif attn_0_1_output in {"4"}:
            return position == 13
        elif attn_0_1_output in {"</s>"}:
            return position == 6
        elif attn_0_1_output in {"<s>"}:
            return position == 5

    num_attn_1_4_pattern = select(positions, attn_0_1_outputs, num_predicate_1_4)
    num_attn_1_4_outputs = aggregate_sum(num_attn_1_4_pattern, num_attn_0_5_outputs)
    num_attn_1_4_output_scores = classifier_weights.loc[
        [("num_attn_1_4_outputs", "_") for v in num_attn_1_4_outputs]
    ].mul(num_attn_1_4_outputs, axis=0)

    # num_attn_1_5 ####################################################
    def num_predicate_1_5(attn_0_7_output, attn_0_4_output):
        if attn_0_7_output in {"0"}:
            return attn_0_4_output == "<pad>"
        elif attn_0_7_output in {"2", "<s>", "</s>", "4", "1"}:
            return attn_0_4_output == ""
        elif attn_0_7_output in {"3"}:
            return attn_0_4_output == "</s>"

    num_attn_1_5_pattern = select(attn_0_4_outputs, attn_0_7_outputs, num_predicate_1_5)
    num_attn_1_5_outputs = aggregate_sum(num_attn_1_5_pattern, num_attn_0_2_outputs)
    num_attn_1_5_output_scores = classifier_weights.loc[
        [("num_attn_1_5_outputs", "_") for v in num_attn_1_5_outputs]
    ].mul(num_attn_1_5_outputs, axis=0)

    # num_attn_1_6 ####################################################
    def num_predicate_1_6(attn_0_2_output, position):
        if attn_0_2_output in {"0", "1"}:
            return position == 15
        elif attn_0_2_output in {"2"}:
            return position == 0
        elif attn_0_2_output in {"3", "4"}:
            return position == 13
        elif attn_0_2_output in {"</s>"}:
            return position == 10
        elif attn_0_2_output in {"<s>"}:
            return position == 9

    num_attn_1_6_pattern = select(positions, attn_0_2_outputs, num_predicate_1_6)
    num_attn_1_6_outputs = aggregate_sum(num_attn_1_6_pattern, num_attn_0_5_outputs)
    num_attn_1_6_output_scores = classifier_weights.loc[
        [("num_attn_1_6_outputs", "_") for v in num_attn_1_6_outputs]
    ].mul(num_attn_1_6_outputs, axis=0)

    # num_attn_1_7 ####################################################
    def num_predicate_1_7(attn_0_2_output, attn_0_7_output):
        if attn_0_2_output in {"3", "0"}:
            return attn_0_7_output == "</s>"
        elif attn_0_2_output in {"</s>", "2", "4", "1"}:
            return attn_0_7_output == ""
        elif attn_0_2_output in {"<s>"}:
            return attn_0_7_output == "<pad>"

    num_attn_1_7_pattern = select(attn_0_7_outputs, attn_0_2_outputs, num_predicate_1_7)
    num_attn_1_7_outputs = aggregate_sum(num_attn_1_7_pattern, num_attn_0_3_outputs)
    num_attn_1_7_output_scores = classifier_weights.loc[
        [("num_attn_1_7_outputs", "_") for v in num_attn_1_7_outputs]
    ].mul(num_attn_1_7_outputs, axis=0)

    # mlp_1_0 #####################################################
    def mlp_1_0(attn_0_3_output, attn_0_4_output):
        key = (attn_0_3_output, attn_0_4_output)
        if key in {("0", "4"), ("1", "4"), ("3", "4"), ("<s>", "4")}:
            return 7
        elif key in {("0", "</s>"), ("1", "</s>"), ("4", "</s>"), ("</s>", "4")}:
            return 8
        elif key in {("</s>", "</s>"), ("</s>", "<s>"), ("<s>", "</s>")}:
            return 5
        elif key in {
            ("4", "0"),
            ("4", "1"),
            ("4", "2"),
            ("4", "3"),
            ("4", "4"),
            ("4", "<s>"),
        }:
            return 14
        elif key in {("2", "</s>"), ("</s>", "2")}:
            return 2
        elif key in {("3", "</s>"), ("</s>", "3")}:
            return 0
        elif key in {("</s>", "0"), ("</s>", "1")}:
            return 10
        return 9

    mlp_1_0_outputs = [
        mlp_1_0(k0, k1) for k0, k1 in zip(attn_0_3_outputs, attn_0_4_outputs)
    ]
    mlp_1_0_output_scores = classifier_weights.loc[
        [("mlp_1_0_outputs", str(v)) for v in mlp_1_0_outputs]
    ]

    # mlp_1_1 #####################################################
    def mlp_1_1(position, attn_0_2_output):
        key = (position, attn_0_2_output)
        if key in {
            (0, "0"),
            (0, "1"),
            (0, "2"),
            (0, "<s>"),
            (1, "0"),
            (1, "1"),
            (1, "2"),
            (1, "<s>"),
            (2, "0"),
            (2, "1"),
            (2, "2"),
            (2, "<s>"),
            (3, "0"),
            (3, "2"),
            (3, "<s>"),
            (5, "0"),
            (5, "2"),
            (5, "<s>"),
            (6, "2"),
            (7, "0"),
            (7, "1"),
            (7, "2"),
            (7, "<s>"),
            (8, "0"),
            (8, "2"),
            (8, "<s>"),
            (9, "0"),
            (9, "1"),
            (9, "2"),
            (9, "<s>"),
            (10, "0"),
            (10, "1"),
            (10, "2"),
            (10, "<s>"),
            (12, "0"),
            (12, "1"),
            (12, "2"),
            (12, "<s>"),
            (13, "0"),
            (13, "1"),
            (13, "2"),
            (13, "<s>"),
            (14, "0"),
            (14, "2"),
            (15, "2"),
        }:
            return 7
        elif key in {
            (0, "3"),
            (0, "4"),
            (1, "3"),
            (1, "4"),
            (2, "3"),
            (2, "4"),
            (7, "3"),
            (7, "4"),
            (9, "3"),
            (9, "4"),
            (10, "3"),
            (10, "4"),
            (11, "3"),
            (11, "4"),
            (11, "<s>"),
            (12, "3"),
            (12, "4"),
            (13, "3"),
            (13, "4"),
            (14, "3"),
            (14, "4"),
            (14, "<s>"),
            (15, "3"),
            (15, "4"),
            (15, "<s>"),
        }:
            return 11
        return 6

    mlp_1_1_outputs = [mlp_1_1(k0, k1) for k0, k1 in zip(positions, attn_0_2_outputs)]
    mlp_1_1_output_scores = classifier_weights.loc[
        [("mlp_1_1_outputs", str(v)) for v in mlp_1_1_outputs]
    ]

    # num_mlp_1_0 #################################################
    def num_mlp_1_0(num_attn_1_6_output, num_attn_1_0_output):
        key = (num_attn_1_6_output, num_attn_1_0_output)
        return 14

    num_mlp_1_0_outputs = [
        num_mlp_1_0(k0, k1)
        for k0, k1 in zip(num_attn_1_6_outputs, num_attn_1_0_outputs)
    ]
    num_mlp_1_0_output_scores = classifier_weights.loc[
        [("num_mlp_1_0_outputs", str(v)) for v in num_mlp_1_0_outputs]
    ]

    # num_mlp_1_1 #################################################
    def num_mlp_1_1(num_attn_1_2_output, num_attn_1_1_output):
        key = (num_attn_1_2_output, num_attn_1_1_output)
        return 2

    num_mlp_1_1_outputs = [
        num_mlp_1_1(k0, k1)
        for k0, k1 in zip(num_attn_1_2_outputs, num_attn_1_1_outputs)
    ]
    num_mlp_1_1_output_scores = classifier_weights.loc[
        [("num_mlp_1_1_outputs", str(v)) for v in num_mlp_1_1_outputs]
    ]

    # attn_2_0 ####################################################
    def predicate_2_0(q_attn_0_7_output, k_attn_0_7_output):
        if q_attn_0_7_output in {"2", "3", "0", "4", "1"}:
            return k_attn_0_7_output == ""
        elif q_attn_0_7_output in {"</s>"}:
            return k_attn_0_7_output == "1"
        elif q_attn_0_7_output in {"<s>"}:
            return k_attn_0_7_output == "<s>"

    attn_2_0_pattern = select_closest(attn_0_7_outputs, attn_0_7_outputs, predicate_2_0)
    attn_2_0_outputs = aggregate(attn_2_0_pattern, attn_1_6_outputs)
    attn_2_0_output_scores = classifier_weights.loc[
        [("attn_2_0_outputs", str(v)) for v in attn_2_0_outputs]
    ]

    # attn_2_1 ####################################################
    def predicate_2_1(q_token, k_token):
        if q_token in {"0", "1"}:
            return k_token == "2"
        elif q_token in {"2", "3"}:
            return k_token == "4"
        elif q_token in {"4"}:
            return k_token == "0"
        elif q_token in {"<s>", "</s>"}:
            return k_token == ""

    attn_2_1_pattern = select_closest(tokens, tokens, predicate_2_1)
    attn_2_1_outputs = aggregate(attn_2_1_pattern, attn_1_0_outputs)
    attn_2_1_output_scores = classifier_weights.loc[
        [("attn_2_1_outputs", str(v)) for v in attn_2_1_outputs]
    ]

    # attn_2_2 ####################################################
    def predicate_2_2(attn_0_1_output, position):
        if attn_0_1_output in {"4", "0"}:
            return position == 15
        elif attn_0_1_output in {"1"}:
            return position == 12
        elif attn_0_1_output in {"2"}:
            return position == 0
        elif attn_0_1_output in {"3"}:
            return position == 14
        elif attn_0_1_output in {"</s>"}:
            return position == 1
        elif attn_0_1_output in {"<s>"}:
            return position == 7

    attn_2_2_pattern = select_closest(positions, attn_0_1_outputs, predicate_2_2)
    attn_2_2_outputs = aggregate(attn_2_2_pattern, attn_1_1_outputs)
    attn_2_2_output_scores = classifier_weights.loc[
        [("attn_2_2_outputs", str(v)) for v in attn_2_2_outputs]
    ]

    # attn_2_3 ####################################################
    def predicate_2_3(attn_0_2_output, position):
        if attn_0_2_output in {"0"}:
            return position == 14
        elif attn_0_2_output in {"2", "</s>", "1"}:
            return position == 7
        elif attn_0_2_output in {"3"}:
            return position == 15
        elif attn_0_2_output in {"4"}:
            return position == 0
        elif attn_0_2_output in {"<s>"}:
            return position == 3

    attn_2_3_pattern = select_closest(positions, attn_0_2_outputs, predicate_2_3)
    attn_2_3_outputs = aggregate(attn_2_3_pattern, attn_1_4_outputs)
    attn_2_3_output_scores = classifier_weights.loc[
        [("attn_2_3_outputs", str(v)) for v in attn_2_3_outputs]
    ]

    # attn_2_4 ####################################################
    def predicate_2_4(attn_0_0_output, token):
        if attn_0_0_output in {"4", "<s>", "0"}:
            return token == "<s>"
        elif attn_0_0_output in {"3", "1"}:
            return token == ""
        elif attn_0_0_output in {"2"}:
            return token == "2"
        elif attn_0_0_output in {"</s>"}:
            return token == "1"

    attn_2_4_pattern = select_closest(tokens, attn_0_0_outputs, predicate_2_4)
    attn_2_4_outputs = aggregate(attn_2_4_pattern, attn_1_1_outputs)
    attn_2_4_output_scores = classifier_weights.loc[
        [("attn_2_4_outputs", str(v)) for v in attn_2_4_outputs]
    ]

    # attn_2_5 ####################################################
    def predicate_2_5(position, token):
        if position in {0, 15}:
            return token == ""
        elif position in {1, 10, 4}:
            return token == "4"
        elif position in {2, 3, 9, 11, 13, 14}:
            return token == "<s>"
        elif position in {8, 5, 6, 7}:
            return token == "</s>"
        elif position in {12}:
            return token == "3"

    attn_2_5_pattern = select_closest(tokens, positions, predicate_2_5)
    attn_2_5_outputs = aggregate(attn_2_5_pattern, attn_1_0_outputs)
    attn_2_5_output_scores = classifier_weights.loc[
        [("attn_2_5_outputs", str(v)) for v in attn_2_5_outputs]
    ]

    # attn_2_6 ####################################################
    def predicate_2_6(attn_0_1_output, token):
        if attn_0_1_output in {"4", "3", "0"}:
            return token == "3"
        elif attn_0_1_output in {"2", "1"}:
            return token == "4"
        elif attn_0_1_output in {"</s>"}:
            return token == "0"
        elif attn_0_1_output in {"<s>"}:
            return token == "2"

    attn_2_6_pattern = select_closest(tokens, attn_0_1_outputs, predicate_2_6)
    attn_2_6_outputs = aggregate(attn_2_6_pattern, attn_1_1_outputs)
    attn_2_6_output_scores = classifier_weights.loc[
        [("attn_2_6_outputs", str(v)) for v in attn_2_6_outputs]
    ]

    # attn_2_7 ####################################################
    def predicate_2_7(attn_0_5_output, position):
        if attn_0_5_output in {"0"}:
            return position == 15
        elif attn_0_5_output in {"3", "<s>", "1"}:
            return position == 7
        elif attn_0_5_output in {"2"}:
            return position == 14
        elif attn_0_5_output in {"4"}:
            return position == 6
        elif attn_0_5_output in {"</s>"}:
            return position == 9

    attn_2_7_pattern = select_closest(positions, attn_0_5_outputs, predicate_2_7)
    attn_2_7_outputs = aggregate(attn_2_7_pattern, attn_1_0_outputs)
    attn_2_7_output_scores = classifier_weights.loc[
        [("attn_2_7_outputs", str(v)) for v in attn_2_7_outputs]
    ]

    # num_attn_2_0 ####################################################
    def num_predicate_2_0(attn_0_2_output, position):
        if attn_0_2_output in {"0"}:
            return position == 11
        elif attn_0_2_output in {"1"}:
            return position == 6
        elif attn_0_2_output in {"2"}:
            return position == 12
        elif attn_0_2_output in {"3"}:
            return position == 14
        elif attn_0_2_output in {"4"}:
            return position == 5
        elif attn_0_2_output in {"<s>", "</s>"}:
            return position == 9

    num_attn_2_0_pattern = select(positions, attn_0_2_outputs, num_predicate_2_0)
    num_attn_2_0_outputs = aggregate_sum(num_attn_2_0_pattern, num_attn_1_2_outputs)
    num_attn_2_0_output_scores = classifier_weights.loc[
        [("num_attn_2_0_outputs", "_") for v in num_attn_2_0_outputs]
    ].mul(num_attn_2_0_outputs, axis=0)

    # num_attn_2_1 ####################################################
    def num_predicate_2_1(attn_0_2_output, num_mlp_0_1_output):
        if attn_0_2_output in {"3", "0", "1"}:
            return num_mlp_0_1_output == 6
        elif attn_0_2_output in {"2"}:
            return num_mlp_0_1_output == 15
        elif attn_0_2_output in {"</s>", "4"}:
            return num_mlp_0_1_output == 13
        elif attn_0_2_output in {"<s>"}:
            return num_mlp_0_1_output == 9

    num_attn_2_1_pattern = select(
        num_mlp_0_1_outputs, attn_0_2_outputs, num_predicate_2_1
    )
    num_attn_2_1_outputs = aggregate_sum(num_attn_2_1_pattern, num_attn_1_3_outputs)
    num_attn_2_1_output_scores = classifier_weights.loc[
        [("num_attn_2_1_outputs", "_") for v in num_attn_2_1_outputs]
    ].mul(num_attn_2_1_outputs, axis=0)

    # num_attn_2_2 ####################################################
    def num_predicate_2_2(position, mlp_0_1_output):
        if position in {0, 10}:
            return mlp_0_1_output == 10
        elif position in {1, 5, 9, 11, 12, 14}:
            return mlp_0_1_output == 9
        elif position in {2}:
            return mlp_0_1_output == 12
        elif position in {3, 6}:
            return mlp_0_1_output == 13
        elif position in {4}:
            return mlp_0_1_output == 4
        elif position in {7}:
            return mlp_0_1_output == 11
        elif position in {8, 15}:
            return mlp_0_1_output == 6
        elif position in {13}:
            return mlp_0_1_output == 14

    num_attn_2_2_pattern = select(mlp_0_1_outputs, positions, num_predicate_2_2)
    num_attn_2_2_outputs = aggregate_sum(num_attn_2_2_pattern, num_attn_1_7_outputs)
    num_attn_2_2_output_scores = classifier_weights.loc[
        [("num_attn_2_2_outputs", "_") for v in num_attn_2_2_outputs]
    ].mul(num_attn_2_2_outputs, axis=0)

    # num_attn_2_3 ####################################################
    def num_predicate_2_3(attn_0_1_output, mlp_1_0_output):
        if attn_0_1_output in {"3", "0", "1"}:
            return mlp_1_0_output == 7
        elif attn_0_1_output in {"2"}:
            return mlp_1_0_output == 15
        elif attn_0_1_output in {"4"}:
            return mlp_1_0_output == 5
        elif attn_0_1_output in {"</s>"}:
            return mlp_1_0_output == 11
        elif attn_0_1_output in {"<s>"}:
            return mlp_1_0_output == 4

    num_attn_2_3_pattern = select(mlp_1_0_outputs, attn_0_1_outputs, num_predicate_2_3)
    num_attn_2_3_outputs = aggregate_sum(num_attn_2_3_pattern, num_attn_1_2_outputs)
    num_attn_2_3_output_scores = classifier_weights.loc[
        [("num_attn_2_3_outputs", "_") for v in num_attn_2_3_outputs]
    ].mul(num_attn_2_3_outputs, axis=0)

    # num_attn_2_4 ####################################################
    def num_predicate_2_4(attn_0_7_output, mlp_1_0_output):
        if attn_0_7_output in {"0"}:
            return mlp_1_0_output == 4
        elif attn_0_7_output in {"3", "4", "1"}:
            return mlp_1_0_output == 6
        elif attn_0_7_output in {"2"}:
            return mlp_1_0_output == 8
        elif attn_0_7_output in {"</s>"}:
            return mlp_1_0_output == 10
        elif attn_0_7_output in {"<s>"}:
            return mlp_1_0_output == 12

    num_attn_2_4_pattern = select(mlp_1_0_outputs, attn_0_7_outputs, num_predicate_2_4)
    num_attn_2_4_outputs = aggregate_sum(num_attn_2_4_pattern, num_attn_1_4_outputs)
    num_attn_2_4_output_scores = classifier_weights.loc[
        [("num_attn_2_4_outputs", "_") for v in num_attn_2_4_outputs]
    ].mul(num_attn_2_4_outputs, axis=0)

    # num_attn_2_5 ####################################################
    def num_predicate_2_5(mlp_1_1_output, num_mlp_0_1_output):
        if mlp_1_1_output in {0}:
            return num_mlp_0_1_output == 11
        elif mlp_1_1_output in {1}:
            return num_mlp_0_1_output == 12
        elif mlp_1_1_output in {2, 4, 9, 12, 15}:
            return num_mlp_0_1_output == 0
        elif mlp_1_1_output in {3, 6}:
            return num_mlp_0_1_output == 8
        elif mlp_1_1_output in {5}:
            return num_mlp_0_1_output == 15
        elif mlp_1_1_output in {14, 7}:
            return num_mlp_0_1_output == 13
        elif mlp_1_1_output in {8, 11}:
            return num_mlp_0_1_output == 10
        elif mlp_1_1_output in {10}:
            return num_mlp_0_1_output == 6
        elif mlp_1_1_output in {13}:
            return num_mlp_0_1_output == 2

    num_attn_2_5_pattern = select(
        num_mlp_0_1_outputs, mlp_1_1_outputs, num_predicate_2_5
    )
    num_attn_2_5_outputs = aggregate_sum(num_attn_2_5_pattern, num_attn_1_0_outputs)
    num_attn_2_5_output_scores = classifier_weights.loc[
        [("num_attn_2_5_outputs", "_") for v in num_attn_2_5_outputs]
    ].mul(num_attn_2_5_outputs, axis=0)

    # num_attn_2_6 ####################################################
    def num_predicate_2_6(mlp_1_1_output, position):
        if mlp_1_1_output in {0, 4, 6, 11, 13, 15}:
            return position == 1
        elif mlp_1_1_output in {1, 7}:
            return position == 10
        elif mlp_1_1_output in {2}:
            return position == 9
        elif mlp_1_1_output in {3}:
            return position == 7
        elif mlp_1_1_output in {9, 12, 5}:
            return position == 6
        elif mlp_1_1_output in {8}:
            return position == 14
        elif mlp_1_1_output in {10}:
            return position == 0
        elif mlp_1_1_output in {14}:
            return position == 4

    num_attn_2_6_pattern = select(positions, mlp_1_1_outputs, num_predicate_2_6)
    num_attn_2_6_outputs = aggregate_sum(num_attn_2_6_pattern, num_attn_1_5_outputs)
    num_attn_2_6_output_scores = classifier_weights.loc[
        [("num_attn_2_6_outputs", "_") for v in num_attn_2_6_outputs]
    ].mul(num_attn_2_6_outputs, axis=0)

    # num_attn_2_7 ####################################################
    def num_predicate_2_7(attn_0_0_output, attn_0_3_output):
        if attn_0_0_output in {"3", "0"}:
            return attn_0_3_output == "</s>"
        elif attn_0_0_output in {"4", "1"}:
            return attn_0_3_output == ""
        elif attn_0_0_output in {"2"}:
            return attn_0_3_output == "<pad>"
        elif attn_0_0_output in {"<s>", "</s>"}:
            return attn_0_3_output == "<s>"

    num_attn_2_7_pattern = select(attn_0_3_outputs, attn_0_0_outputs, num_predicate_2_7)
    num_attn_2_7_outputs = aggregate_sum(num_attn_2_7_pattern, num_attn_0_6_outputs)
    num_attn_2_7_output_scores = classifier_weights.loc[
        [("num_attn_2_7_outputs", "_") for v in num_attn_2_7_outputs]
    ].mul(num_attn_2_7_outputs, axis=0)

    # mlp_2_0 #####################################################
    def mlp_2_0(attn_0_4_output, attn_0_3_output):
        key = (attn_0_4_output, attn_0_3_output)
        if key in {
            ("0", "0"),
            ("0", "1"),
            ("0", "2"),
            ("0", "4"),
            ("0", "<s>"),
            ("1", "0"),
            ("1", "1"),
            ("1", "2"),
            ("1", "4"),
            ("1", "<s>"),
            ("2", "0"),
            ("2", "1"),
            ("2", "2"),
            ("2", "4"),
            ("2", "<s>"),
            ("3", "0"),
            ("3", "1"),
            ("3", "2"),
            ("3", "4"),
            ("3", "<s>"),
            ("4", "0"),
            ("4", "1"),
            ("4", "2"),
            ("4", "4"),
            ("4", "<s>"),
            ("<s>", "0"),
            ("<s>", "1"),
            ("<s>", "2"),
            ("<s>", "4"),
            ("<s>", "<s>"),
        }:
            return 14
        elif key in {
            ("0", "3"),
            ("1", "3"),
            ("2", "3"),
            ("3", "3"),
            ("3", "</s>"),
            ("4", "3"),
            ("</s>", "3"),
            ("<s>", "3"),
        }:
            return 8
        elif key in {("0", "</s>"), ("1", "</s>"), ("2", "</s>"), ("<s>", "</s>")}:
            return 6
        return 9

    mlp_2_0_outputs = [
        mlp_2_0(k0, k1) for k0, k1 in zip(attn_0_4_outputs, attn_0_3_outputs)
    ]
    mlp_2_0_output_scores = classifier_weights.loc[
        [("mlp_2_0_outputs", str(v)) for v in mlp_2_0_outputs]
    ]

    # mlp_2_1 #####################################################
    def mlp_2_1(mlp_1_0_output, num_mlp_1_0_output):
        key = (mlp_1_0_output, num_mlp_1_0_output)
        return 9

    mlp_2_1_outputs = [
        mlp_2_1(k0, k1) for k0, k1 in zip(mlp_1_0_outputs, num_mlp_1_0_outputs)
    ]
    mlp_2_1_output_scores = classifier_weights.loc[
        [("mlp_2_1_outputs", str(v)) for v in mlp_2_1_outputs]
    ]

    # num_mlp_2_0 #################################################
    def num_mlp_2_0(num_attn_1_3_output, num_attn_1_5_output):
        key = (num_attn_1_3_output, num_attn_1_5_output)
        if key in {
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1),
            (2, 0),
            (2, 1),
            (3, 0),
            (3, 1),
            (4, 0),
            (4, 1),
            (5, 0),
            (5, 1),
            (6, 0),
            (6, 1),
            (7, 0),
            (7, 1),
            (8, 0),
            (8, 1),
            (9, 0),
            (9, 1),
            (10, 0),
            (10, 1),
            (11, 0),
            (11, 1),
            (12, 0),
            (12, 1),
            (13, 0),
            (13, 1),
            (14, 0),
            (14, 1),
            (15, 0),
            (15, 1),
            (16, 0),
            (16, 1),
            (17, 0),
            (17, 1),
            (18, 0),
            (18, 1),
            (19, 0),
            (19, 1),
            (20, 0),
            (20, 1),
            (21, 0),
            (21, 1),
            (22, 0),
            (22, 1),
            (23, 0),
            (23, 1),
            (24, 0),
            (24, 1),
            (25, 0),
            (25, 1),
            (26, 0),
            (26, 1),
            (27, 0),
            (27, 1),
            (28, 0),
            (28, 1),
            (29, 0),
            (29, 1),
            (30, 0),
            (30, 1),
            (30, 2),
            (31, 0),
            (31, 1),
            (31, 2),
            (32, 0),
            (32, 1),
            (32, 2),
            (33, 0),
            (33, 1),
            (33, 2),
            (34, 0),
            (34, 1),
            (34, 2),
            (35, 0),
            (35, 1),
            (35, 2),
            (36, 0),
            (36, 1),
            (36, 2),
            (37, 0),
            (37, 1),
            (37, 2),
            (38, 0),
            (38, 1),
            (38, 2),
            (39, 0),
            (39, 1),
            (39, 2),
            (40, 0),
            (40, 1),
            (40, 2),
            (41, 0),
            (41, 1),
            (41, 2),
            (42, 0),
            (42, 1),
            (42, 2),
            (43, 0),
            (43, 1),
            (43, 2),
            (44, 0),
            (44, 1),
            (44, 2),
            (45, 0),
            (45, 1),
            (45, 2),
            (46, 0),
            (46, 1),
            (46, 2),
            (47, 0),
            (47, 1),
            (47, 2),
        }:
            return 13
        return 1

    num_mlp_2_0_outputs = [
        num_mlp_2_0(k0, k1)
        for k0, k1 in zip(num_attn_1_3_outputs, num_attn_1_5_outputs)
    ]
    num_mlp_2_0_output_scores = classifier_weights.loc[
        [("num_mlp_2_0_outputs", str(v)) for v in num_mlp_2_0_outputs]
    ]

    # num_mlp_2_1 #################################################
    def num_mlp_2_1(num_attn_2_1_output, num_attn_1_0_output):
        key = (num_attn_2_1_output, num_attn_1_0_output)
        return 0

    num_mlp_2_1_outputs = [
        num_mlp_2_1(k0, k1)
        for k0, k1 in zip(num_attn_2_1_outputs, num_attn_1_0_outputs)
    ]
    num_mlp_2_1_output_scores = classifier_weights.loc[
        [("num_mlp_2_1_outputs", str(v)) for v in num_mlp_2_1_outputs]
    ]

    feature_logits = pd.concat(
        [
            df.reset_index()
            for df in [
                token_scores,
                position_scores,
                attn_0_0_output_scores,
                attn_0_1_output_scores,
                attn_0_2_output_scores,
                attn_0_3_output_scores,
                attn_0_4_output_scores,
                attn_0_5_output_scores,
                attn_0_6_output_scores,
                attn_0_7_output_scores,
                mlp_0_0_output_scores,
                mlp_0_1_output_scores,
                num_mlp_0_0_output_scores,
                num_mlp_0_1_output_scores,
                attn_1_0_output_scores,
                attn_1_1_output_scores,
                attn_1_2_output_scores,
                attn_1_3_output_scores,
                attn_1_4_output_scores,
                attn_1_5_output_scores,
                attn_1_6_output_scores,
                attn_1_7_output_scores,
                mlp_1_0_output_scores,
                mlp_1_1_output_scores,
                num_mlp_1_0_output_scores,
                num_mlp_1_1_output_scores,
                attn_2_0_output_scores,
                attn_2_1_output_scores,
                attn_2_2_output_scores,
                attn_2_3_output_scores,
                attn_2_4_output_scores,
                attn_2_5_output_scores,
                attn_2_6_output_scores,
                attn_2_7_output_scores,
                mlp_2_0_output_scores,
                mlp_2_1_output_scores,
                num_mlp_2_0_output_scores,
                num_mlp_2_1_output_scores,
                one_scores,
                num_attn_0_0_output_scores,
                num_attn_0_1_output_scores,
                num_attn_0_2_output_scores,
                num_attn_0_3_output_scores,
                num_attn_0_4_output_scores,
                num_attn_0_5_output_scores,
                num_attn_0_6_output_scores,
                num_attn_0_7_output_scores,
                num_attn_1_0_output_scores,
                num_attn_1_1_output_scores,
                num_attn_1_2_output_scores,
                num_attn_1_3_output_scores,
                num_attn_1_4_output_scores,
                num_attn_1_5_output_scores,
                num_attn_1_6_output_scores,
                num_attn_1_7_output_scores,
                num_attn_2_0_output_scores,
                num_attn_2_1_output_scores,
                num_attn_2_2_output_scores,
                num_attn_2_3_output_scores,
                num_attn_2_4_output_scores,
                num_attn_2_5_output_scores,
                num_attn_2_6_output_scores,
                num_attn_2_7_output_scores,
            ]
        ]
    )
    logits = feature_logits.groupby(level=0).sum(numeric_only=True).to_numpy()
    classes = classifier_weights.columns.to_numpy()
    predictions = classes[logits.argmax(-1)]
    if tokens[0] == "<s>":
        predictions[0] = "<s>"
    if tokens[-1] == "</s>":
        predictions[-1] = "</s>"
    return predictions.tolist()


print(run(["<s>", "0", "4", "3", "3", "0", "1", "1", "4", "2", "</s>"]))
