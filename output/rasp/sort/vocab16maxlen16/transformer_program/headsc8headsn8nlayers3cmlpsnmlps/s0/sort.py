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
        "output/rasp/sort/vocab16maxlen16/transformer_program/headsc8headsn8nlayers3cmlpsnmlps/s0/sort_weights.csv",
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
            return k_position == 2
        elif q_position in {1, 6}:
            return k_position == 5
        elif q_position in {2}:
            return k_position == 4
        elif q_position in {3, 4}:
            return k_position == 1
        elif q_position in {5}:
            return k_position == 3
        elif q_position in {15, 7}:
            return k_position == 6
        elif q_position in {8}:
            return k_position == 7
        elif q_position in {9, 13}:
            return k_position == 12
        elif q_position in {10, 11}:
            return k_position == 9
        elif q_position in {12}:
            return k_position == 11
        elif q_position in {14}:
            return k_position == 13

    attn_0_0_pattern = select_closest(positions, positions, predicate_0_0)
    attn_0_0_outputs = aggregate(attn_0_0_pattern, tokens)
    attn_0_0_output_scores = classifier_weights.loc[
        [("attn_0_0_outputs", str(v)) for v in attn_0_0_outputs]
    ]

    # attn_0_1 ####################################################
    def predicate_0_1(position, token):
        if position in {0}:
            return token == "1"
        elif position in {1}:
            return token == "0"
        elif position in {11, 2, 10, 15}:
            return token == "3"
        elif position in {3}:
            return token == "9"
        elif position in {4}:
            return token == "2"
        elif position in {5, 6, 7}:
            return token == "5"
        elif position in {8, 9, 13, 14}:
            return token == "8"
        elif position in {12}:
            return token == "7"

    attn_0_1_pattern = select_closest(tokens, positions, predicate_0_1)
    attn_0_1_outputs = aggregate(attn_0_1_pattern, tokens)
    attn_0_1_output_scores = classifier_weights.loc[
        [("attn_0_1_outputs", str(v)) for v in attn_0_1_outputs]
    ]

    # attn_0_2 ####################################################
    def predicate_0_2(position, token):
        if position in {0, 13}:
            return token == "7"
        elif position in {1, 14}:
            return token == "10"
        elif position in {8, 9, 2, 7}:
            return token == "4"
        elif position in {3, 4}:
            return token == "5"
        elif position in {11, 5}:
            return token == "9"
        elif position in {6}:
            return token == "8"
        elif position in {10, 15}:
            return token == "12"
        elif position in {12}:
            return token == "3"

    attn_0_2_pattern = select_closest(tokens, positions, predicate_0_2)
    attn_0_2_outputs = aggregate(attn_0_2_pattern, tokens)
    attn_0_2_output_scores = classifier_weights.loc[
        [("attn_0_2_outputs", str(v)) for v in attn_0_2_outputs]
    ]

    # attn_0_3 ####################################################
    def predicate_0_3(position, token):
        if position in {0}:
            return token == "6"
        elif position in {1}:
            return token == "1"
        elif position in {2}:
            return token == "2"
        elif position in {3, 6, 15}:
            return token == "4"
        elif position in {10, 4, 5, 14}:
            return token == "9"
        elif position in {8, 12, 13, 7}:
            return token == "8"
        elif position in {9, 11}:
            return token == "5"

    attn_0_3_pattern = select_closest(tokens, positions, predicate_0_3)
    attn_0_3_outputs = aggregate(attn_0_3_pattern, tokens)
    attn_0_3_output_scores = classifier_weights.loc[
        [("attn_0_3_outputs", str(v)) for v in attn_0_3_outputs]
    ]

    # attn_0_4 ####################################################
    def predicate_0_4(q_position, k_position):
        if q_position in {0}:
            return k_position == 2
        elif q_position in {1, 4, 6}:
            return k_position == 3
        elif q_position in {2, 15}:
            return k_position == 1
        elif q_position in {3}:
            return k_position == 5
        elif q_position in {8, 5}:
            return k_position == 4
        elif q_position in {11, 12, 7}:
            return k_position == 10
        elif q_position in {9, 10}:
            return k_position == 8
        elif q_position in {13}:
            return k_position == 11
        elif q_position in {14}:
            return k_position == 7

    attn_0_4_pattern = select_closest(positions, positions, predicate_0_4)
    attn_0_4_outputs = aggregate(attn_0_4_pattern, tokens)
    attn_0_4_output_scores = classifier_weights.loc[
        [("attn_0_4_outputs", str(v)) for v in attn_0_4_outputs]
    ]

    # attn_0_5 ####################################################
    def predicate_0_5(position, token):
        if position in {0, 2, 4, 5, 6, 7, 8, 10, 11}:
            return token == "7"
        elif position in {1}:
            return token == "5"
        elif position in {3}:
            return token == "12"
        elif position in {9}:
            return token == "3"
        elif position in {12}:
            return token == "9"
        elif position in {13, 14}:
            return token == "4"
        elif position in {15}:
            return token == "11"

    attn_0_5_pattern = select_closest(tokens, positions, predicate_0_5)
    attn_0_5_outputs = aggregate(attn_0_5_pattern, tokens)
    attn_0_5_output_scores = classifier_weights.loc[
        [("attn_0_5_outputs", str(v)) for v in attn_0_5_outputs]
    ]

    # attn_0_6 ####################################################
    def predicate_0_6(q_position, k_position):
        if q_position in {0}:
            return k_position == 1
        elif q_position in {1}:
            return k_position == 2
        elif q_position in {2}:
            return k_position == 3
        elif q_position in {3}:
            return k_position == 4
        elif q_position in {4}:
            return k_position == 5
        elif q_position in {5}:
            return k_position == 6
        elif q_position in {6}:
            return k_position == 7
        elif q_position in {7}:
            return k_position == 8
        elif q_position in {8}:
            return k_position == 9
        elif q_position in {9}:
            return k_position == 10
        elif q_position in {10}:
            return k_position == 11
        elif q_position in {11}:
            return k_position == 12
        elif q_position in {12, 14}:
            return k_position == 13
        elif q_position in {13, 15}:
            return k_position == 14

    attn_0_6_pattern = select_closest(positions, positions, predicate_0_6)
    attn_0_6_outputs = aggregate(attn_0_6_pattern, tokens)
    attn_0_6_output_scores = classifier_weights.loc[
        [("attn_0_6_outputs", str(v)) for v in attn_0_6_outputs]
    ]

    # attn_0_7 ####################################################
    def predicate_0_7(position, token):
        if position in {0, 9, 6, 7}:
            return token == "1"
        elif position in {1}:
            return token == "10"
        elif position in {2, 3}:
            return token == "0"
        elif position in {4, 5, 14}:
            return token == "8"
        elif position in {8, 10}:
            return token == "5"
        elif position in {11, 12, 13}:
            return token == "9"
        elif position in {15}:
            return token == "3"

    attn_0_7_pattern = select_closest(tokens, positions, predicate_0_7)
    attn_0_7_outputs = aggregate(attn_0_7_pattern, tokens)
    attn_0_7_output_scores = classifier_weights.loc[
        [("attn_0_7_outputs", str(v)) for v in attn_0_7_outputs]
    ]

    # num_attn_0_0 ####################################################
    def num_predicate_0_0(position, token):
        if position in {0}:
            return token == "1"
        elif position in {1, 2}:
            return token == "12"
        elif position in {3, 4, 5, 6}:
            return token == "11"
        elif position in {10, 11, 15, 7}:
            return token == "10"
        elif position in {8, 9}:
            return token == "0"
        elif position in {12, 13}:
            return token == "9"
        elif position in {14}:
            return token == "8"

    num_attn_0_0_pattern = select(tokens, positions, num_predicate_0_0)
    num_attn_0_0_outputs = aggregate_sum(num_attn_0_0_pattern, ones)
    num_attn_0_0_output_scores = classifier_weights.loc[
        [("num_attn_0_0_outputs", "_") for v in num_attn_0_0_outputs]
    ].mul(num_attn_0_0_outputs, axis=0)

    # num_attn_0_1 ####################################################
    def num_predicate_0_1(position, token):
        if position in {0}:
            return token == "10"
        elif position in {1, 2, 10, 13, 15}:
            return token == "0"
        elif position in {3, 4, 5, 6}:
            return token == "2"
        elif position in {9, 7}:
            return token == "12"
        elif position in {8, 12}:
            return token == "1"
        elif position in {11}:
            return token == "11"
        elif position in {14}:
            return token == "<pad>"

    num_attn_0_1_pattern = select(tokens, positions, num_predicate_0_1)
    num_attn_0_1_outputs = aggregate_sum(num_attn_0_1_pattern, ones)
    num_attn_0_1_output_scores = classifier_weights.loc[
        [("num_attn_0_1_outputs", "_") for v in num_attn_0_1_outputs]
    ].mul(num_attn_0_1_outputs, axis=0)

    # num_attn_0_2 ####################################################
    def num_predicate_0_2(position, token):
        if position in {0, 1, 11}:
            return token == "0"
        elif position in {2}:
            return token == "<s>"
        elif position in {3, 4, 5, 6}:
            return token == "12"
        elif position in {7}:
            return token == "11"
        elif position in {8, 9, 12}:
            return token == "10"
        elif position in {10, 13}:
            return token == "1"
        elif position in {14, 15}:
            return token == "<pad>"

    num_attn_0_2_pattern = select(tokens, positions, num_predicate_0_2)
    num_attn_0_2_outputs = aggregate_sum(num_attn_0_2_pattern, ones)
    num_attn_0_2_output_scores = classifier_weights.loc[
        [("num_attn_0_2_outputs", "_") for v in num_attn_0_2_outputs]
    ].mul(num_attn_0_2_outputs, axis=0)

    # num_attn_0_3 ####################################################
    def num_predicate_0_3(q_position, k_position):
        if q_position in {0, 5}:
            return k_position == 8
        elif q_position in {1}:
            return k_position == 3
        elif q_position in {2, 3}:
            return k_position == 5
        elif q_position in {4}:
            return k_position == 6
        elif q_position in {6}:
            return k_position == 9
        elif q_position in {15, 7}:
            return k_position == 10
        elif q_position in {8}:
            return k_position == 11
        elif q_position in {9}:
            return k_position == 12
        elif q_position in {10, 13}:
            return k_position == 13
        elif q_position in {11}:
            return k_position == 14
        elif q_position in {12}:
            return k_position == 15
        elif q_position in {14}:
            return k_position == 0

    num_attn_0_3_pattern = select(positions, positions, num_predicate_0_3)
    num_attn_0_3_outputs = aggregate_sum(num_attn_0_3_pattern, ones)
    num_attn_0_3_output_scores = classifier_weights.loc[
        [("num_attn_0_3_outputs", "_") for v in num_attn_0_3_outputs]
    ].mul(num_attn_0_3_outputs, axis=0)

    # num_attn_0_4 ####################################################
    def num_predicate_0_4(position, token):
        if position in {0, 8, 9}:
            return token == "1"
        elif position in {1, 2}:
            return token == "11"
        elif position in {3, 4, 5, 6}:
            return token == "10"
        elif position in {15, 7}:
            return token == "0"
        elif position in {10, 11, 12}:
            return token == "9"
        elif position in {13}:
            return token == "8"
        elif position in {14}:
            return token == "4"

    num_attn_0_4_pattern = select(tokens, positions, num_predicate_0_4)
    num_attn_0_4_outputs = aggregate_sum(num_attn_0_4_pattern, ones)
    num_attn_0_4_output_scores = classifier_weights.loc[
        [("num_attn_0_4_outputs", "_") for v in num_attn_0_4_outputs]
    ].mul(num_attn_0_4_outputs, axis=0)

    # num_attn_0_5 ####################################################
    def num_predicate_0_5(q_position, k_position):
        if q_position in {0, 8, 10, 11, 13}:
            return k_position == 9
        elif q_position in {1}:
            return k_position == 5
        elif q_position in {2}:
            return k_position == 7
        elif q_position in {3, 14}:
            return k_position == 8
        elif q_position in {9, 4}:
            return k_position == 10
        elif q_position in {5, 7}:
            return k_position == 15
        elif q_position in {6}:
            return k_position == 14
        elif q_position in {12}:
            return k_position == 12
        elif q_position in {15}:
            return k_position == 11

    num_attn_0_5_pattern = select(positions, positions, num_predicate_0_5)
    num_attn_0_5_outputs = aggregate_sum(num_attn_0_5_pattern, ones)
    num_attn_0_5_output_scores = classifier_weights.loc[
        [("num_attn_0_5_outputs", "_") for v in num_attn_0_5_outputs]
    ].mul(num_attn_0_5_outputs, axis=0)

    # num_attn_0_6 ####################################################
    def num_predicate_0_6(position, token):
        if position in {0, 2}:
            return token == "10"
        elif position in {1, 10, 15}:
            return token == "11"
        elif position in {3, 7}:
            return token == "1"
        elif position in {4, 5, 6}:
            return token == "0"
        elif position in {8}:
            return token == "3"
        elif position in {9, 13}:
            return token == "2"
        elif position in {11}:
            return token == "12"
        elif position in {12, 14}:
            return token == "</s>"

    num_attn_0_6_pattern = select(tokens, positions, num_predicate_0_6)
    num_attn_0_6_outputs = aggregate_sum(num_attn_0_6_pattern, ones)
    num_attn_0_6_output_scores = classifier_weights.loc[
        [("num_attn_0_6_outputs", "_") for v in num_attn_0_6_outputs]
    ].mul(num_attn_0_6_outputs, axis=0)

    # num_attn_0_7 ####################################################
    def num_predicate_0_7(q_position, k_position):
        if q_position in {0, 6, 15}:
            return k_position == 10
        elif q_position in {1}:
            return k_position == 1
        elif q_position in {2, 3}:
            return k_position == 6
        elif q_position in {4, 13}:
            return k_position == 7
        elif q_position in {5}:
            return k_position == 9
        elif q_position in {14, 7}:
            return k_position == 11
        elif q_position in {8}:
            return k_position == 12
        elif q_position in {9, 10}:
            return k_position == 14
        elif q_position in {11}:
            return k_position == 15
        elif q_position in {12}:
            return k_position == 13

    num_attn_0_7_pattern = select(positions, positions, num_predicate_0_7)
    num_attn_0_7_outputs = aggregate_sum(num_attn_0_7_pattern, ones)
    num_attn_0_7_output_scores = classifier_weights.loc[
        [("num_attn_0_7_outputs", "_") for v in num_attn_0_7_outputs]
    ].mul(num_attn_0_7_outputs, axis=0)

    # mlp_0_0 #####################################################
    def mlp_0_0(attn_0_6_output, position):
        key = (attn_0_6_output, position)
        if key in {
            ("0", 1),
            ("0", 2),
            ("0", 15),
            ("1", 1),
            ("1", 2),
            ("1", 15),
            ("10", 1),
            ("10", 2),
            ("11", 1),
            ("11", 2),
            ("12", 1),
            ("12", 2),
            ("2", 1),
            ("2", 2),
            ("3", 1),
            ("3", 2),
            ("3", 15),
            ("4", 1),
            ("4", 2),
            ("5", 1),
            ("5", 2),
            ("5", 15),
            ("6", 1),
            ("6", 2),
            ("6", 15),
            ("7", 1),
            ("7", 2),
            ("7", 15),
            ("8", 1),
            ("8", 2),
            ("8", 15),
            ("9", 1),
            ("9", 2),
            ("9", 15),
            ("</s>", 1),
            ("</s>", 2),
            ("<s>", 1),
            ("<s>", 2),
        }:
            return 5
        elif key in {
            ("0", 3),
            ("0", 4),
            ("1", 3),
            ("1", 4),
            ("10", 3),
            ("10", 4),
            ("11", 3),
            ("11", 4),
            ("12", 3),
            ("12", 4),
            ("2", 3),
            ("2", 4),
            ("3", 3),
            ("3", 4),
            ("4", 3),
            ("4", 4),
            ("5", 3),
            ("5", 4),
            ("6", 3),
            ("6", 4),
            ("7", 3),
            ("7", 4),
            ("8", 3),
            ("8", 4),
            ("9", 3),
            ("9", 4),
            ("<s>", 4),
        }:
            return 15
        elif key in {("</s>", 3), ("</s>", 4), ("</s>", 15), ("<s>", 3)}:
            return 8
        elif key in {("<s>", 15)}:
            return 0
        return 3

    mlp_0_0_outputs = [mlp_0_0(k0, k1) for k0, k1 in zip(attn_0_6_outputs, positions)]
    mlp_0_0_output_scores = classifier_weights.loc[
        [("mlp_0_0_outputs", str(v)) for v in mlp_0_0_outputs]
    ]

    # mlp_0_1 #####################################################
    def mlp_0_1(position):
        key = position
        if key in {1, 2, 3, 15}:
            return 11
        elif key in {4}:
            return 4
        elif key in {5}:
            return 9
        return 8

    mlp_0_1_outputs = [mlp_0_1(k0) for k0 in positions]
    mlp_0_1_output_scores = classifier_weights.loc[
        [("mlp_0_1_outputs", str(v)) for v in mlp_0_1_outputs]
    ]

    # mlp_0_2 #####################################################
    def mlp_0_2(attn_0_7_output, position):
        key = (attn_0_7_output, position)
        if key in {
            ("1", 2),
            ("1", 3),
            ("1", 4),
            ("1", 14),
            ("1", 15),
            ("10", 2),
            ("10", 3),
            ("10", 4),
            ("10", 14),
            ("10", 15),
            ("11", 2),
            ("11", 3),
            ("11", 4),
            ("11", 15),
            ("12", 2),
            ("12", 3),
            ("12", 4),
            ("12", 15),
            ("2", 2),
            ("2", 3),
            ("2", 4),
            ("2", 15),
            ("3", 2),
            ("3", 3),
            ("3", 4),
            ("3", 15),
            ("4", 2),
            ("4", 3),
            ("4", 4),
            ("4", 15),
            ("5", 2),
            ("5", 3),
            ("5", 4),
            ("5", 15),
            ("6", 2),
            ("6", 3),
            ("6", 4),
            ("6", 15),
            ("7", 2),
            ("7", 3),
            ("7", 4),
            ("7", 15),
            ("8", 2),
            ("8", 3),
            ("8", 4),
            ("8", 15),
            ("9", 2),
            ("9", 3),
            ("9", 4),
            ("9", 15),
            ("</s>", 2),
            ("</s>", 3),
            ("</s>", 4),
            ("</s>", 15),
            ("<s>", 2),
            ("<s>", 3),
            ("<s>", 4),
            ("<s>", 15),
        }:
            return 4
        elif key in {
            ("0", 1),
            ("0", 2),
            ("1", 1),
            ("10", 1),
            ("11", 1),
            ("12", 1),
            ("2", 1),
            ("3", 1),
            ("4", 1),
            ("5", 1),
            ("6", 1),
            ("7", 1),
            ("8", 1),
            ("9", 1),
            ("</s>", 1),
            ("<s>", 1),
        }:
            return 7
        elif key in {("0", 3), ("0", 4), ("0", 11), ("0", 15)}:
            return 2
        return 8

    mlp_0_2_outputs = [mlp_0_2(k0, k1) for k0, k1 in zip(attn_0_7_outputs, positions)]
    mlp_0_2_output_scores = classifier_weights.loc[
        [("mlp_0_2_outputs", str(v)) for v in mlp_0_2_outputs]
    ]

    # mlp_0_3 #####################################################
    def mlp_0_3(position, attn_0_1_output):
        key = (position, attn_0_1_output)
        if key in {
            (0, "12"),
            (0, "4"),
            (0, "6"),
            (0, "7"),
            (0, "8"),
            (0, "9"),
            (0, "</s>"),
            (5, "0"),
            (5, "1"),
            (5, "10"),
            (5, "11"),
            (5, "12"),
            (5, "2"),
            (5, "3"),
            (5, "4"),
            (5, "5"),
            (5, "6"),
            (5, "7"),
            (5, "8"),
            (5, "9"),
            (5, "</s>"),
            (5, "<s>"),
            (6, "0"),
            (6, "1"),
            (6, "10"),
            (6, "11"),
            (6, "12"),
            (6, "2"),
            (6, "3"),
            (6, "4"),
            (6, "5"),
            (6, "6"),
            (6, "7"),
            (6, "8"),
            (6, "9"),
            (6, "</s>"),
            (6, "<s>"),
        }:
            return 10
        elif key in {
            (0, "0"),
            (0, "1"),
            (0, "10"),
            (0, "11"),
            (0, "2"),
            (0, "3"),
            (0, "5"),
            (0, "<s>"),
            (1, "0"),
            (1, "1"),
            (1, "10"),
            (1, "11"),
            (1, "12"),
            (1, "2"),
            (1, "3"),
            (1, "4"),
            (1, "5"),
            (1, "6"),
            (1, "7"),
            (1, "8"),
            (1, "9"),
            (1, "</s>"),
            (1, "<s>"),
            (2, "0"),
            (2, "1"),
            (2, "10"),
            (2, "11"),
            (2, "12"),
            (2, "2"),
            (2, "3"),
            (2, "4"),
            (2, "5"),
            (2, "6"),
            (2, "7"),
            (2, "8"),
            (2, "9"),
            (2, "</s>"),
            (2, "<s>"),
        }:
            return 13
        elif key in {
            (3, "0"),
            (3, "1"),
            (3, "10"),
            (3, "11"),
            (3, "12"),
            (3, "2"),
            (3, "3"),
            (3, "4"),
            (3, "5"),
            (3, "6"),
            (3, "7"),
            (3, "8"),
            (3, "9"),
            (3, "</s>"),
            (3, "<s>"),
            (4, "0"),
            (4, "1"),
            (4, "10"),
            (4, "11"),
            (4, "12"),
            (4, "2"),
            (4, "3"),
            (4, "4"),
            (4, "5"),
            (4, "6"),
            (4, "7"),
            (4, "8"),
            (4, "9"),
            (4, "</s>"),
            (4, "<s>"),
        }:
            return 2
        return 12

    mlp_0_3_outputs = [mlp_0_3(k0, k1) for k0, k1 in zip(positions, attn_0_1_outputs)]
    mlp_0_3_output_scores = classifier_weights.loc[
        [("mlp_0_3_outputs", str(v)) for v in mlp_0_3_outputs]
    ]

    # num_mlp_0_0 #################################################
    def num_mlp_0_0(num_attn_0_5_output, num_attn_0_6_output):
        key = (num_attn_0_5_output, num_attn_0_6_output)
        if key in {
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
        }:
            return 3
        elif key in {(0, 0)}:
            return 8
        return 0

    num_mlp_0_0_outputs = [
        num_mlp_0_0(k0, k1)
        for k0, k1 in zip(num_attn_0_5_outputs, num_attn_0_6_outputs)
    ]
    num_mlp_0_0_output_scores = classifier_weights.loc[
        [("num_mlp_0_0_outputs", str(v)) for v in num_mlp_0_0_outputs]
    ]

    # num_mlp_0_1 #################################################
    def num_mlp_0_1(num_attn_0_0_output, num_attn_0_7_output):
        key = (num_attn_0_0_output, num_attn_0_7_output)
        if key in {(0, 1), (1, 0)}:
            return 3
        elif key in {(0, 0)}:
            return 7
        return 8

    num_mlp_0_1_outputs = [
        num_mlp_0_1(k0, k1)
        for k0, k1 in zip(num_attn_0_0_outputs, num_attn_0_7_outputs)
    ]
    num_mlp_0_1_output_scores = classifier_weights.loc[
        [("num_mlp_0_1_outputs", str(v)) for v in num_mlp_0_1_outputs]
    ]

    # num_mlp_0_2 #################################################
    def num_mlp_0_2(num_attn_0_4_output, num_attn_0_0_output):
        key = (num_attn_0_4_output, num_attn_0_0_output)
        return 1

    num_mlp_0_2_outputs = [
        num_mlp_0_2(k0, k1)
        for k0, k1 in zip(num_attn_0_4_outputs, num_attn_0_0_outputs)
    ]
    num_mlp_0_2_output_scores = classifier_weights.loc[
        [("num_mlp_0_2_outputs", str(v)) for v in num_mlp_0_2_outputs]
    ]

    # num_mlp_0_3 #################################################
    def num_mlp_0_3(num_attn_0_7_output, num_attn_0_3_output):
        key = (num_attn_0_7_output, num_attn_0_3_output)
        if key in {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)}:
            return 2
        return 5

    num_mlp_0_3_outputs = [
        num_mlp_0_3(k0, k1)
        for k0, k1 in zip(num_attn_0_7_outputs, num_attn_0_3_outputs)
    ]
    num_mlp_0_3_output_scores = classifier_weights.loc[
        [("num_mlp_0_3_outputs", str(v)) for v in num_mlp_0_3_outputs]
    ]

    # attn_1_0 ####################################################
    def predicate_1_0(position, num_mlp_0_1_output):
        if position in {0}:
            return num_mlp_0_1_output == 11
        elif position in {1, 2, 6, 9, 11, 15}:
            return num_mlp_0_1_output == 3
        elif position in {3, 4}:
            return num_mlp_0_1_output == 7
        elif position in {8, 5, 7}:
            return num_mlp_0_1_output == 8
        elif position in {10, 12}:
            return num_mlp_0_1_output == 1
        elif position in {13}:
            return num_mlp_0_1_output == 13
        elif position in {14}:
            return num_mlp_0_1_output == 5

    attn_1_0_pattern = select_closest(num_mlp_0_1_outputs, positions, predicate_1_0)
    attn_1_0_outputs = aggregate(attn_1_0_pattern, tokens)
    attn_1_0_output_scores = classifier_weights.loc[
        [("attn_1_0_outputs", str(v)) for v in attn_1_0_outputs]
    ]

    # attn_1_1 ####################################################
    def predicate_1_1(position, token):
        if position in {0, 12}:
            return token == "7"
        elif position in {1, 2, 13}:
            return token == "2"
        elif position in {3, 5}:
            return token == "11"
        elif position in {4}:
            return token == "8"
        elif position in {6, 7}:
            return token == "10"
        elif position in {8}:
            return token == "12"
        elif position in {9, 10, 14}:
            return token == "3"
        elif position in {11}:
            return token == "0"
        elif position in {15}:
            return token == "<s>"

    attn_1_1_pattern = select_closest(tokens, positions, predicate_1_1)
    attn_1_1_outputs = aggregate(attn_1_1_pattern, attn_0_6_outputs)
    attn_1_1_output_scores = classifier_weights.loc[
        [("attn_1_1_outputs", str(v)) for v in attn_1_1_outputs]
    ]

    # attn_1_2 ####################################################
    def predicate_1_2(position, token):
        if position in {0, 1}:
            return token == "1"
        elif position in {2}:
            return token == "10"
        elif position in {9, 3, 6, 7}:
            return token == "3"
        elif position in {4, 5}:
            return token == "4"
        elif position in {8}:
            return token == "11"
        elif position in {10, 11, 14}:
            return token == "9"
        elif position in {12, 13}:
            return token == "8"
        elif position in {15}:
            return token == "12"

    attn_1_2_pattern = select_closest(tokens, positions, predicate_1_2)
    attn_1_2_outputs = aggregate(attn_1_2_pattern, tokens)
    attn_1_2_output_scores = classifier_weights.loc[
        [("attn_1_2_outputs", str(v)) for v in attn_1_2_outputs]
    ]

    # attn_1_3 ####################################################
    def predicate_1_3(token, mlp_0_3_output):
        if token in {"2", "0"}:
            return mlp_0_3_output == 2
        elif token in {"1"}:
            return mlp_0_3_output == 5
        elif token in {"10", "4"}:
            return mlp_0_3_output == 10
        elif token in {"5", "11"}:
            return mlp_0_3_output == 14
        elif token in {"12"}:
            return mlp_0_3_output == 12
        elif token in {"3"}:
            return mlp_0_3_output == 6
        elif token in {"6"}:
            return mlp_0_3_output == 13
        elif token in {"7"}:
            return mlp_0_3_output == 1
        elif token in {"</s>", "8"}:
            return mlp_0_3_output == 8
        elif token in {"9"}:
            return mlp_0_3_output == 15
        elif token in {"<s>"}:
            return mlp_0_3_output == 9

    attn_1_3_pattern = select_closest(mlp_0_3_outputs, tokens, predicate_1_3)
    attn_1_3_outputs = aggregate(attn_1_3_pattern, attn_0_5_outputs)
    attn_1_3_output_scores = classifier_weights.loc[
        [("attn_1_3_outputs", str(v)) for v in attn_1_3_outputs]
    ]

    # attn_1_4 ####################################################
    def predicate_1_4(q_token, k_token):
        if q_token in {"0"}:
            return k_token == "4"
        elif q_token in {"3", "7", "1"}:
            return k_token == "6"
        elif q_token in {"12", "10", "4"}:
            return k_token == "5"
        elif q_token in {"11"}:
            return k_token == "2"
        elif q_token in {"2"}:
            return k_token == "8"
        elif q_token in {"5"}:
            return k_token == "12"
        elif q_token in {"6"}:
            return k_token == "<pad>"
        elif q_token in {"8", "9"}:
            return k_token == "3"
        elif q_token in {"</s>"}:
            return k_token == "1"
        elif q_token in {"<s>"}:
            return k_token == "9"

    attn_1_4_pattern = select_closest(tokens, tokens, predicate_1_4)
    attn_1_4_outputs = aggregate(attn_1_4_pattern, attn_0_6_outputs)
    attn_1_4_output_scores = classifier_weights.loc[
        [("attn_1_4_outputs", str(v)) for v in attn_1_4_outputs]
    ]

    # attn_1_5 ####################################################
    def predicate_1_5(position, token):
        if position in {0, 1, 3}:
            return token == "2"
        elif position in {2}:
            return token == "1"
        elif position in {4, 5}:
            return token == "3"
        elif position in {6, 7, 8, 9, 12, 13, 14}:
            return token == "9"
        elif position in {10, 11}:
            return token == "8"
        elif position in {15}:
            return token == "5"

    attn_1_5_pattern = select_closest(tokens, positions, predicate_1_5)
    attn_1_5_outputs = aggregate(attn_1_5_pattern, tokens)
    attn_1_5_output_scores = classifier_weights.loc[
        [("attn_1_5_outputs", str(v)) for v in attn_1_5_outputs]
    ]

    # attn_1_6 ####################################################
    def predicate_1_6(q_token, k_token):
        if q_token in {"2", "0"}:
            return k_token == "12"
        elif q_token in {"1"}:
            return k_token == "11"
        elif q_token in {"10"}:
            return k_token == "3"
        elif q_token in {"11"}:
            return k_token == "0"
        elif q_token in {"12", "3", "4"}:
            return k_token == "5"
        elif q_token in {"5"}:
            return k_token == "4"
        elif q_token in {"6", "7", "8"}:
            return k_token == "2"
        elif q_token in {"9"}:
            return k_token == "</s>"
        elif q_token in {"</s>"}:
            return k_token == "10"
        elif q_token in {"<s>"}:
            return k_token == "1"

    attn_1_6_pattern = select_closest(tokens, tokens, predicate_1_6)
    attn_1_6_outputs = aggregate(attn_1_6_pattern, attn_0_0_outputs)
    attn_1_6_output_scores = classifier_weights.loc[
        [("attn_1_6_outputs", str(v)) for v in attn_1_6_outputs]
    ]

    # attn_1_7 ####################################################
    def predicate_1_7(q_token, k_token):
        if q_token in {"7", "1", "10", "0", "5"}:
            return k_token == "3"
        elif q_token in {"11"}:
            return k_token == "8"
        elif q_token in {"12", "9"}:
            return k_token == "4"
        elif q_token in {"2"}:
            return k_token == "11"
        elif q_token in {"3", "8"}:
            return k_token == "9"
        elif q_token in {"6", "4"}:
            return k_token == "5"
        elif q_token in {"<s>", "</s>"}:
            return k_token == "1"

    attn_1_7_pattern = select_closest(tokens, tokens, predicate_1_7)
    attn_1_7_outputs = aggregate(attn_1_7_pattern, attn_0_6_outputs)
    attn_1_7_output_scores = classifier_weights.loc[
        [("attn_1_7_outputs", str(v)) for v in attn_1_7_outputs]
    ]

    # num_attn_1_0 ####################################################
    def num_predicate_1_0(attn_0_4_output, attn_0_6_output):
        if attn_0_4_output in {"0"}:
            return attn_0_6_output == "0"
        elif attn_0_4_output in {"1", "10", "<s>", "</s>", "11"}:
            return attn_0_6_output == "1"
        elif attn_0_4_output in {"12", "4"}:
            return attn_0_6_output == "12"
        elif attn_0_4_output in {"2"}:
            return attn_0_6_output == "2"
        elif attn_0_4_output in {"3", "7", "8"}:
            return attn_0_6_output == "11"
        elif attn_0_4_output in {"5"}:
            return attn_0_6_output == "5"
        elif attn_0_4_output in {"6"}:
            return attn_0_6_output == "10"
        elif attn_0_4_output in {"9"}:
            return attn_0_6_output == "3"

    num_attn_1_0_pattern = select(attn_0_6_outputs, attn_0_4_outputs, num_predicate_1_0)
    num_attn_1_0_outputs = aggregate_sum(num_attn_1_0_pattern, num_attn_0_6_outputs)
    num_attn_1_0_output_scores = classifier_weights.loc[
        [("num_attn_1_0_outputs", "_") for v in num_attn_1_0_outputs]
    ].mul(num_attn_1_0_outputs, axis=0)

    # num_attn_1_1 ####################################################
    def num_predicate_1_1(attn_0_6_output, token):
        if attn_0_6_output in {"0", "8"}:
            return token == "0"
        elif attn_0_6_output in {"</s>", "5", "1"}:
            return token == "1"
        elif attn_0_6_output in {"10", "<s>"}:
            return token == "10"
        elif attn_0_6_output in {"2", "6", "3", "11", "9"}:
            return token == "11"
        elif attn_0_6_output in {"12"}:
            return token == "12"
        elif attn_0_6_output in {"7", "4"}:
            return token == "4"

    num_attn_1_1_pattern = select(tokens, attn_0_6_outputs, num_predicate_1_1)
    num_attn_1_1_outputs = aggregate_sum(num_attn_1_1_pattern, num_attn_0_6_outputs)
    num_attn_1_1_output_scores = classifier_weights.loc[
        [("num_attn_1_1_outputs", "_") for v in num_attn_1_1_outputs]
    ].mul(num_attn_1_1_outputs, axis=0)

    # num_attn_1_2 ####################################################
    def num_predicate_1_2(mlp_0_1_output, attn_0_7_output):
        if mlp_0_1_output in {0, 8, 6}:
            return attn_0_7_output == "3"
        elif mlp_0_1_output in {1, 12}:
            return attn_0_7_output == "10"
        elif mlp_0_1_output in {2, 5}:
            return attn_0_7_output == "4"
        elif mlp_0_1_output in {3}:
            return attn_0_7_output == "5"
        elif mlp_0_1_output in {4, 7, 9, 11, 13, 15}:
            return attn_0_7_output == "1"
        elif mlp_0_1_output in {10, 14}:
            return attn_0_7_output == "0"

    num_attn_1_2_pattern = select(attn_0_7_outputs, mlp_0_1_outputs, num_predicate_1_2)
    num_attn_1_2_outputs = aggregate_sum(num_attn_1_2_pattern, num_attn_0_4_outputs)
    num_attn_1_2_output_scores = classifier_weights.loc[
        [("num_attn_1_2_outputs", "_") for v in num_attn_1_2_outputs]
    ].mul(num_attn_1_2_outputs, axis=0)

    # num_attn_1_3 ####################################################
    def num_predicate_1_3(position, attn_0_1_output):
        if position in {0, 1, 11, 15}:
            return attn_0_1_output == "1"
        elif position in {2, 3}:
            return attn_0_1_output == "0"
        elif position in {4, 5, 6, 7, 9, 10}:
            return attn_0_1_output == "2"
        elif position in {8}:
            return attn_0_1_output == "12"
        elif position in {12, 13, 14}:
            return attn_0_1_output == "<pad>"

    num_attn_1_3_pattern = select(attn_0_1_outputs, positions, num_predicate_1_3)
    num_attn_1_3_outputs = aggregate_sum(num_attn_1_3_pattern, num_attn_0_1_outputs)
    num_attn_1_3_output_scores = classifier_weights.loc[
        [("num_attn_1_3_outputs", "_") for v in num_attn_1_3_outputs]
    ].mul(num_attn_1_3_outputs, axis=0)

    # num_attn_1_4 ####################################################
    def num_predicate_1_4(position, mlp_0_1_output):
        if position in {0, 9, 2}:
            return mlp_0_1_output == 11
        elif position in {1}:
            return mlp_0_1_output == 14
        elif position in {3, 4, 5, 6, 7, 8}:
            return mlp_0_1_output == 8
        elif position in {10}:
            return mlp_0_1_output == 3
        elif position in {11}:
            return mlp_0_1_output == 5
        elif position in {12}:
            return mlp_0_1_output == 7
        elif position in {13}:
            return mlp_0_1_output == 6
        elif position in {14}:
            return mlp_0_1_output == 10
        elif position in {15}:
            return mlp_0_1_output == 9

    num_attn_1_4_pattern = select(mlp_0_1_outputs, positions, num_predicate_1_4)
    num_attn_1_4_outputs = aggregate_sum(num_attn_1_4_pattern, num_attn_0_6_outputs)
    num_attn_1_4_output_scores = classifier_weights.loc[
        [("num_attn_1_4_outputs", "_") for v in num_attn_1_4_outputs]
    ].mul(num_attn_1_4_outputs, axis=0)

    # num_attn_1_5 ####################################################
    def num_predicate_1_5(mlp_0_1_output, token):
        if mlp_0_1_output in {0, 2, 3, 6, 8, 9, 10, 12, 15}:
            return token == "12"
        elif mlp_0_1_output in {1, 14}:
            return token == "2"
        elif mlp_0_1_output in {4}:
            return token == "<s>"
        elif mlp_0_1_output in {13, 11, 5, 7}:
            return token == "1"

    num_attn_1_5_pattern = select(tokens, mlp_0_1_outputs, num_predicate_1_5)
    num_attn_1_5_outputs = aggregate_sum(num_attn_1_5_pattern, num_attn_0_0_outputs)
    num_attn_1_5_output_scores = classifier_weights.loc[
        [("num_attn_1_5_outputs", "_") for v in num_attn_1_5_outputs]
    ].mul(num_attn_1_5_outputs, axis=0)

    # num_attn_1_6 ####################################################
    def num_predicate_1_6(position, mlp_0_1_output):
        if position in {0, 2, 3, 4, 5, 6, 7}:
            return mlp_0_1_output == 8
        elif position in {1}:
            return mlp_0_1_output == 11
        elif position in {8, 9}:
            return mlp_0_1_output == 3
        elif position in {10}:
            return mlp_0_1_output == 5
        elif position in {11, 12}:
            return mlp_0_1_output == 7
        elif position in {13}:
            return mlp_0_1_output == 13
        elif position in {14}:
            return mlp_0_1_output == 1
        elif position in {15}:
            return mlp_0_1_output == 4

    num_attn_1_6_pattern = select(mlp_0_1_outputs, positions, num_predicate_1_6)
    num_attn_1_6_outputs = aggregate_sum(num_attn_1_6_pattern, num_attn_0_2_outputs)
    num_attn_1_6_output_scores = classifier_weights.loc[
        [("num_attn_1_6_outputs", "_") for v in num_attn_1_6_outputs]
    ].mul(num_attn_1_6_outputs, axis=0)

    # num_attn_1_7 ####################################################
    def num_predicate_1_7(attn_0_2_output, token):
        if attn_0_2_output in {
            "2",
            "6",
            "7",
            "1",
            "12",
            "</s>",
            "0",
            "<s>",
            "4",
            "3",
            "5",
            "8",
            "9",
        }:
            return token == "11"
        elif attn_0_2_output in {"10", "11"}:
            return token == "1"

    num_attn_1_7_pattern = select(tokens, attn_0_2_outputs, num_predicate_1_7)
    num_attn_1_7_outputs = aggregate_sum(num_attn_1_7_pattern, num_attn_0_0_outputs)
    num_attn_1_7_output_scores = classifier_weights.loc[
        [("num_attn_1_7_outputs", "_") for v in num_attn_1_7_outputs]
    ].mul(num_attn_1_7_outputs, axis=0)

    # mlp_1_0 #####################################################
    def mlp_1_0(attn_1_3_output, attn_1_0_output):
        key = (attn_1_3_output, attn_1_0_output)
        if key in {("10", "0"), ("10", "1"), ("10", "12"), ("10", "6")}:
            return 9
        return 14

    mlp_1_0_outputs = [
        mlp_1_0(k0, k1) for k0, k1 in zip(attn_1_3_outputs, attn_1_0_outputs)
    ]
    mlp_1_0_output_scores = classifier_weights.loc[
        [("mlp_1_0_outputs", str(v)) for v in mlp_1_0_outputs]
    ]

    # mlp_1_1 #####################################################
    def mlp_1_1(position, attn_1_3_output):
        key = (position, attn_1_3_output)
        if key in {
            (0, "0"),
            (0, "1"),
            (0, "10"),
            (0, "11"),
            (1, "0"),
            (1, "1"),
            (1, "10"),
            (1, "11"),
            (1, "12"),
            (1, "2"),
            (1, "3"),
            (1, "4"),
            (1, "5"),
            (1, "6"),
            (1, "7"),
            (1, "8"),
            (1, "9"),
            (1, "</s>"),
            (1, "<s>"),
            (2, "0"),
            (2, "1"),
            (2, "10"),
            (2, "11"),
            (2, "12"),
            (2, "2"),
            (2, "3"),
            (2, "4"),
            (2, "5"),
            (2, "6"),
            (2, "7"),
            (2, "8"),
            (2, "9"),
            (2, "</s>"),
            (2, "<s>"),
            (3, "0"),
            (3, "1"),
            (3, "10"),
            (3, "11"),
            (3, "12"),
            (3, "2"),
            (3, "3"),
            (3, "4"),
            (3, "5"),
            (3, "6"),
            (3, "7"),
            (3, "8"),
            (3, "9"),
            (3, "</s>"),
            (3, "<s>"),
            (8, "10"),
            (8, "11"),
            (12, "11"),
            (15, "0"),
            (15, "1"),
            (15, "10"),
            (15, "11"),
            (15, "2"),
            (15, "3"),
            (15, "<s>"),
        }:
            return 5
        elif key in {
            (6, "0"),
            (6, "1"),
            (6, "10"),
            (6, "11"),
            (6, "12"),
            (6, "2"),
            (6, "3"),
            (6, "4"),
            (6, "5"),
            (6, "6"),
            (6, "7"),
            (6, "8"),
            (6, "9"),
            (6, "</s>"),
            (6, "<s>"),
            (8, "0"),
            (8, "1"),
            (8, "12"),
            (8, "3"),
            (8, "5"),
            (8, "6"),
            (8, "7"),
            (8, "</s>"),
            (8, "<s>"),
            (11, "0"),
            (11, "1"),
            (11, "10"),
            (11, "12"),
            (11, "3"),
            (11, "5"),
            (11, "6"),
            (11, "7"),
            (11, "</s>"),
            (11, "<s>"),
        }:
            return 9
        return 8

    mlp_1_1_outputs = [mlp_1_1(k0, k1) for k0, k1 in zip(positions, attn_1_3_outputs)]
    mlp_1_1_output_scores = classifier_weights.loc[
        [("mlp_1_1_outputs", str(v)) for v in mlp_1_1_outputs]
    ]

    # mlp_1_2 #####################################################
    def mlp_1_2(position, attn_1_0_output):
        key = (position, attn_1_0_output)
        if key in {
            (0, "1"),
            (0, "2"),
            (0, "3"),
            (0, "</s>"),
            (2, "0"),
            (2, "1"),
            (2, "10"),
            (2, "11"),
            (2, "12"),
            (2, "2"),
            (2, "3"),
            (2, "5"),
            (2, "6"),
            (2, "7"),
            (2, "8"),
            (2, "9"),
            (2, "</s>"),
            (2, "<s>"),
            (3, "0"),
            (3, "1"),
            (3, "10"),
            (3, "11"),
            (3, "12"),
            (3, "2"),
            (3, "3"),
            (3, "4"),
            (3, "5"),
            (3, "6"),
            (3, "7"),
            (3, "8"),
            (3, "9"),
            (3, "</s>"),
            (3, "<s>"),
            (4, "1"),
            (4, "10"),
            (4, "11"),
            (4, "12"),
            (4, "</s>"),
            (5, "0"),
            (5, "1"),
            (5, "2"),
            (5, "3"),
            (5, "</s>"),
            (6, "1"),
            (9, "1"),
            (11, "0"),
            (11, "1"),
            (11, "2"),
            (11, "3"),
            (11, "</s>"),
            (11, "<s>"),
            (12, "0"),
            (12, "1"),
            (12, "2"),
            (12, "3"),
            (12, "</s>"),
            (13, "1"),
            (14, "1"),
            (14, "11"),
            (15, "1"),
            (15, "10"),
            (15, "</s>"),
        }:
            return 0
        elif key in {
            (0, "0"),
            (0, "5"),
            (0, "<s>"),
            (2, "4"),
            (4, "0"),
            (4, "2"),
            (4, "3"),
            (4, "4"),
            (4, "5"),
            (4, "6"),
            (4, "7"),
            (4, "8"),
            (4, "<s>"),
            (5, "5"),
            (5, "<s>"),
            (6, "0"),
            (6, "2"),
            (6, "3"),
            (6, "5"),
            (6, "</s>"),
            (6, "<s>"),
            (7, "0"),
            (8, "0"),
            (9, "0"),
            (9, "2"),
            (9, "3"),
            (9, "</s>"),
            (9, "<s>"),
            (10, "0"),
            (10, "2"),
            (10, "3"),
            (10, "</s>"),
            (10, "<s>"),
            (12, "5"),
            (12, "<s>"),
            (13, "0"),
            (13, "2"),
            (13, "3"),
            (13, "</s>"),
            (13, "<s>"),
            (14, "0"),
            (14, "10"),
            (14, "12"),
            (14, "2"),
            (14, "3"),
            (14, "4"),
            (14, "5"),
            (14, "7"),
            (14, "8"),
            (14, "</s>"),
            (14, "<s>"),
            (15, "0"),
            (15, "11"),
            (15, "12"),
            (15, "2"),
            (15, "3"),
            (15, "4"),
            (15, "5"),
            (15, "<s>"),
        }:
            return 1
        elif key in {
            (1, "0"),
            (1, "1"),
            (1, "10"),
            (1, "11"),
            (1, "12"),
            (1, "2"),
            (1, "3"),
            (1, "4"),
            (1, "5"),
            (1, "6"),
            (1, "7"),
            (1, "8"),
            (1, "9"),
            (1, "</s>"),
            (1, "<s>"),
        }:
            return 10
        return 9

    mlp_1_2_outputs = [mlp_1_2(k0, k1) for k0, k1 in zip(positions, attn_1_0_outputs)]
    mlp_1_2_output_scores = classifier_weights.loc[
        [("mlp_1_2_outputs", str(v)) for v in mlp_1_2_outputs]
    ]

    # mlp_1_3 #####################################################
    def mlp_1_3(attn_1_3_output, position):
        key = (attn_1_3_output, position)
        if key in {
            ("0", 8),
            ("0", 13),
            ("0", 14),
            ("1", 13),
            ("10", 13),
            ("10", 14),
            ("11", 13),
            ("12", 0),
            ("12", 4),
            ("12", 8),
            ("12", 10),
            ("12", 11),
            ("12", 12),
            ("12", 13),
            ("12", 14),
            ("12", 15),
            ("2", 0),
            ("2", 8),
            ("2", 11),
            ("2", 12),
            ("2", 13),
            ("2", 14),
            ("2", 15),
            ("3", 8),
            ("3", 13),
            ("3", 14),
            ("4", 13),
            ("4", 14),
            ("5", 0),
            ("5", 2),
            ("5", 4),
            ("5", 5),
            ("5", 6),
            ("5", 7),
            ("5", 8),
            ("5", 9),
            ("5", 10),
            ("5", 11),
            ("5", 12),
            ("5", 13),
            ("5", 14),
            ("5", 15),
            ("6", 0),
            ("6", 4),
            ("6", 5),
            ("6", 8),
            ("6", 9),
            ("6", 10),
            ("6", 11),
            ("6", 12),
            ("6", 13),
            ("6", 14),
            ("6", 15),
            ("7", 0),
            ("7", 4),
            ("7", 5),
            ("7", 8),
            ("7", 9),
            ("7", 10),
            ("7", 11),
            ("7", 12),
            ("7", 13),
            ("7", 14),
            ("7", 15),
            ("8", 0),
            ("8", 4),
            ("8", 5),
            ("8", 8),
            ("8", 10),
            ("8", 11),
            ("8", 12),
            ("8", 13),
            ("8", 14),
            ("8", 15),
            ("9", 8),
            ("9", 11),
            ("9", 12),
            ("9", 13),
            ("9", 14),
            ("9", 15),
            ("</s>", 0),
            ("</s>", 4),
            ("</s>", 8),
            ("</s>", 10),
            ("</s>", 11),
            ("</s>", 12),
            ("</s>", 13),
            ("</s>", 14),
            ("</s>", 15),
            ("<s>", 8),
            ("<s>", 11),
            ("<s>", 12),
            ("<s>", 13),
            ("<s>", 14),
        }:
            return 4
        elif key in {
            ("0", 1),
            ("1", 1),
            ("10", 1),
            ("11", 1),
            ("12", 1),
            ("2", 1),
            ("3", 1),
            ("4", 1),
            ("5", 1),
            ("6", 1),
            ("7", 1),
            ("8", 1),
            ("9", 1),
            ("</s>", 1),
            ("<s>", 1),
        }:
            return 3
        return 6

    mlp_1_3_outputs = [mlp_1_3(k0, k1) for k0, k1 in zip(attn_1_3_outputs, positions)]
    mlp_1_3_output_scores = classifier_weights.loc[
        [("mlp_1_3_outputs", str(v)) for v in mlp_1_3_outputs]
    ]

    # num_mlp_1_0 #################################################
    def num_mlp_1_0(num_attn_1_1_output, num_attn_1_3_output):
        key = (num_attn_1_1_output, num_attn_1_3_output)
        return 7

    num_mlp_1_0_outputs = [
        num_mlp_1_0(k0, k1)
        for k0, k1 in zip(num_attn_1_1_outputs, num_attn_1_3_outputs)
    ]
    num_mlp_1_0_output_scores = classifier_weights.loc[
        [("num_mlp_1_0_outputs", str(v)) for v in num_mlp_1_0_outputs]
    ]

    # num_mlp_1_1 #################################################
    def num_mlp_1_1(num_attn_1_2_output):
        key = num_attn_1_2_output
        return 2

    num_mlp_1_1_outputs = [num_mlp_1_1(k0) for k0 in num_attn_1_2_outputs]
    num_mlp_1_1_output_scores = classifier_weights.loc[
        [("num_mlp_1_1_outputs", str(v)) for v in num_mlp_1_1_outputs]
    ]

    # num_mlp_1_2 #################################################
    def num_mlp_1_2(num_attn_1_0_output, num_attn_1_2_output):
        key = (num_attn_1_0_output, num_attn_1_2_output)
        return 10

    num_mlp_1_2_outputs = [
        num_mlp_1_2(k0, k1)
        for k0, k1 in zip(num_attn_1_0_outputs, num_attn_1_2_outputs)
    ]
    num_mlp_1_2_output_scores = classifier_weights.loc[
        [("num_mlp_1_2_outputs", str(v)) for v in num_mlp_1_2_outputs]
    ]

    # num_mlp_1_3 #################################################
    def num_mlp_1_3(num_attn_1_3_output):
        key = num_attn_1_3_output
        if key in {0}:
            return 12
        return 0

    num_mlp_1_3_outputs = [num_mlp_1_3(k0) for k0 in num_attn_1_3_outputs]
    num_mlp_1_3_output_scores = classifier_weights.loc[
        [("num_mlp_1_3_outputs", str(v)) for v in num_mlp_1_3_outputs]
    ]

    # attn_2_0 ####################################################
    def predicate_2_0(mlp_0_3_output, token):
        if mlp_0_3_output in {0, 3, 13, 15}:
            return token == "</s>"
        elif mlp_0_3_output in {1}:
            return token == "6"
        elif mlp_0_3_output in {2, 4, 7}:
            return token == "<s>"
        elif mlp_0_3_output in {8, 5}:
            return token == "5"
        elif mlp_0_3_output in {12, 6}:
            return token == "3"
        elif mlp_0_3_output in {9}:
            return token == "4"
        elif mlp_0_3_output in {10, 11}:
            return token == "10"
        elif mlp_0_3_output in {14}:
            return token == "<pad>"

    attn_2_0_pattern = select_closest(tokens, mlp_0_3_outputs, predicate_2_0)
    attn_2_0_outputs = aggregate(attn_2_0_pattern, attn_0_4_outputs)
    attn_2_0_output_scores = classifier_weights.loc[
        [("attn_2_0_outputs", str(v)) for v in attn_2_0_outputs]
    ]

    # attn_2_1 ####################################################
    def predicate_2_1(q_token, k_token):
        if q_token in {"0"}:
            return k_token == "2"
        elif q_token in {"9", "1"}:
            return k_token == "3"
        elif q_token in {"10", "11"}:
            return k_token == "9"
        elif q_token in {"12", "4"}:
            return k_token == "8"
        elif q_token in {"2", "3"}:
            return k_token == "5"
        elif q_token in {"</s>", "5", "<s>"}:
            return k_token == "<pad>"
        elif q_token in {"6"}:
            return k_token == "11"
        elif q_token in {"7", "8"}:
            return k_token == "10"

    attn_2_1_pattern = select_closest(tokens, tokens, predicate_2_1)
    attn_2_1_outputs = aggregate(attn_2_1_pattern, attn_1_6_outputs)
    attn_2_1_output_scores = classifier_weights.loc[
        [("attn_2_1_outputs", str(v)) for v in attn_2_1_outputs]
    ]

    # attn_2_2 ####################################################
    def predicate_2_2(mlp_0_0_output, token):
        if mlp_0_0_output in {0, 1, 10}:
            return token == "4"
        elif mlp_0_0_output in {2, 4, 6}:
            return token == "5"
        elif mlp_0_0_output in {3}:
            return token == "6"
        elif mlp_0_0_output in {11, 15, 5, 7}:
            return token == "11"
        elif mlp_0_0_output in {8}:
            return token == "<pad>"
        elif mlp_0_0_output in {9}:
            return token == "10"
        elif mlp_0_0_output in {12}:
            return token == "1"
        elif mlp_0_0_output in {13, 14}:
            return token == "12"

    attn_2_2_pattern = select_closest(tokens, mlp_0_0_outputs, predicate_2_2)
    attn_2_2_outputs = aggregate(attn_2_2_pattern, tokens)
    attn_2_2_output_scores = classifier_weights.loc[
        [("attn_2_2_outputs", str(v)) for v in attn_2_2_outputs]
    ]

    # attn_2_3 ####################################################
    def predicate_2_3(q_token, k_token):
        if q_token in {"6", "1", "12", "0", "3", "5", "8"}:
            return k_token == "</s>"
        elif q_token in {"2", "10"}:
            return k_token == "4"
        elif q_token in {"11"}:
            return k_token == "8"
        elif q_token in {"4"}:
            return k_token == "2"
        elif q_token in {"7"}:
            return k_token == "5"
        elif q_token in {"9"}:
            return k_token == "0"
        elif q_token in {"</s>"}:
            return k_token == "3"
        elif q_token in {"<s>"}:
            return k_token == "<pad>"

    attn_2_3_pattern = select_closest(tokens, tokens, predicate_2_3)
    attn_2_3_outputs = aggregate(attn_2_3_pattern, attn_0_4_outputs)
    attn_2_3_output_scores = classifier_weights.loc[
        [("attn_2_3_outputs", str(v)) for v in attn_2_3_outputs]
    ]

    # attn_2_4 ####################################################
    def predicate_2_4(num_mlp_0_3_output, mlp_0_2_output):
        if num_mlp_0_3_output in {0}:
            return mlp_0_2_output == 14
        elif num_mlp_0_3_output in {1, 7}:
            return mlp_0_2_output == 5
        elif num_mlp_0_3_output in {2}:
            return mlp_0_2_output == 15
        elif num_mlp_0_3_output in {8, 3, 12, 13}:
            return mlp_0_2_output == 9
        elif num_mlp_0_3_output in {4}:
            return mlp_0_2_output == 6
        elif num_mlp_0_3_output in {5, 15}:
            return mlp_0_2_output == 8
        elif num_mlp_0_3_output in {6}:
            return mlp_0_2_output == 11
        elif num_mlp_0_3_output in {9}:
            return mlp_0_2_output == 13
        elif num_mlp_0_3_output in {10}:
            return mlp_0_2_output == 7
        elif num_mlp_0_3_output in {11}:
            return mlp_0_2_output == 4
        elif num_mlp_0_3_output in {14}:
            return mlp_0_2_output == 2

    attn_2_4_pattern = select_closest(
        mlp_0_2_outputs, num_mlp_0_3_outputs, predicate_2_4
    )
    attn_2_4_outputs = aggregate(attn_2_4_pattern, attn_0_0_outputs)
    attn_2_4_output_scores = classifier_weights.loc[
        [("attn_2_4_outputs", str(v)) for v in attn_2_4_outputs]
    ]

    # attn_2_5 ####################################################
    def predicate_2_5(q_token, k_token):
        if q_token in {"2", "6", "7", "1", "12", "0", "4", "3", "5", "8", "11"}:
            return k_token == "</s>"
        elif q_token in {"10"}:
            return k_token == "8"
        elif q_token in {"9"}:
            return k_token == "1"
        elif q_token in {"<s>", "</s>"}:
            return k_token == "<pad>"

    attn_2_5_pattern = select_closest(tokens, tokens, predicate_2_5)
    attn_2_5_outputs = aggregate(attn_2_5_pattern, attn_0_0_outputs)
    attn_2_5_output_scores = classifier_weights.loc[
        [("attn_2_5_outputs", str(v)) for v in attn_2_5_outputs]
    ]

    # attn_2_6 ####################################################
    def predicate_2_6(q_token, k_token):
        if q_token in {"0"}:
            return k_token == "3"
        elif q_token in {"2", "5", "1"}:
            return k_token == "4"
        elif q_token in {"10"}:
            return k_token == "6"
        elif q_token in {"11"}:
            return k_token == "7"
        elif q_token in {"12"}:
            return k_token == "0"
        elif q_token in {"3", "7"}:
            return k_token == "5"
        elif q_token in {"4"}:
            return k_token == "9"
        elif q_token in {"6"}:
            return k_token == "8"
        elif q_token in {"8"}:
            return k_token == "12"
        elif q_token in {"9"}:
            return k_token == "2"
        elif q_token in {"<s>", "</s>"}:
            return k_token == "<pad>"

    attn_2_6_pattern = select_closest(tokens, tokens, predicate_2_6)
    attn_2_6_outputs = aggregate(attn_2_6_pattern, attn_1_1_outputs)
    attn_2_6_output_scores = classifier_weights.loc[
        [("attn_2_6_outputs", str(v)) for v in attn_2_6_outputs]
    ]

    # attn_2_7 ####################################################
    def predicate_2_7(mlp_0_2_output, token):
        if mlp_0_2_output in {0, 4, 8, 12, 15}:
            return token == "9"
        elif mlp_0_2_output in {1, 7}:
            return token == "12"
        elif mlp_0_2_output in {2, 10}:
            return token == "5"
        elif mlp_0_2_output in {11, 3}:
            return token == "<pad>"
        elif mlp_0_2_output in {5, 6}:
            return token == "10"
        elif mlp_0_2_output in {9}:
            return token == "2"
        elif mlp_0_2_output in {13}:
            return token == "11"
        elif mlp_0_2_output in {14}:
            return token == "6"

    attn_2_7_pattern = select_closest(tokens, mlp_0_2_outputs, predicate_2_7)
    attn_2_7_outputs = aggregate(attn_2_7_pattern, attn_0_4_outputs)
    attn_2_7_output_scores = classifier_weights.loc[
        [("attn_2_7_outputs", str(v)) for v in attn_2_7_outputs]
    ]

    # num_attn_2_0 ####################################################
    def num_predicate_2_0(mlp_0_1_output, token):
        if mlp_0_1_output in {0, 3, 7}:
            return token == "1"
        elif mlp_0_1_output in {8, 1, 2}:
            return token == "4"
        elif mlp_0_1_output in {4}:
            return token == "</s>"
        elif mlp_0_1_output in {13, 11, 5}:
            return token == "0"
        elif mlp_0_1_output in {6, 15}:
            return token == "11"
        elif mlp_0_1_output in {9}:
            return token == "<s>"
        elif mlp_0_1_output in {10}:
            return token == "5"
        elif mlp_0_1_output in {12}:
            return token == "3"
        elif mlp_0_1_output in {14}:
            return token == "10"

    num_attn_2_0_pattern = select(tokens, mlp_0_1_outputs, num_predicate_2_0)
    num_attn_2_0_outputs = aggregate_sum(num_attn_2_0_pattern, num_attn_1_1_outputs)
    num_attn_2_0_output_scores = classifier_weights.loc[
        [("num_attn_2_0_outputs", "_") for v in num_attn_2_0_outputs]
    ].mul(num_attn_2_0_outputs, axis=0)

    # num_attn_2_1 ####################################################
    def num_predicate_2_1(mlp_0_1_output, token):
        if mlp_0_1_output in {0, 9, 10, 15}:
            return token == "0"
        elif mlp_0_1_output in {1, 2, 5, 7, 12, 13, 14}:
            return token == "11"
        elif mlp_0_1_output in {3}:
            return token == "10"
        elif mlp_0_1_output in {11, 4}:
            return token == "1"
        elif mlp_0_1_output in {6}:
            return token == "2"
        elif mlp_0_1_output in {8}:
            return token == "<pad>"

    num_attn_2_1_pattern = select(tokens, mlp_0_1_outputs, num_predicate_2_1)
    num_attn_2_1_outputs = aggregate_sum(num_attn_2_1_pattern, num_attn_1_1_outputs)
    num_attn_2_1_output_scores = classifier_weights.loc[
        [("num_attn_2_1_outputs", "_") for v in num_attn_2_1_outputs]
    ].mul(num_attn_2_1_outputs, axis=0)

    # num_attn_2_2 ####################################################
    def num_predicate_2_2(position, token):
        if position in {0, 15}:
            return token == "11"
        elif position in {1, 10}:
            return token == "</s>"
        elif position in {2}:
            return token == "<s>"
        elif position in {8, 3}:
            return token == "10"
        elif position in {4, 5, 6}:
            return token == "1"
        elif position in {7}:
            return token == "12"
        elif position in {9}:
            return token == "0"
        elif position in {11}:
            return token == "4"
        elif position in {12, 13, 14}:
            return token == "<pad>"

    num_attn_2_2_pattern = select(tokens, positions, num_predicate_2_2)
    num_attn_2_2_outputs = aggregate_sum(num_attn_2_2_pattern, num_attn_1_0_outputs)
    num_attn_2_2_output_scores = classifier_weights.loc[
        [("num_attn_2_2_outputs", "_") for v in num_attn_2_2_outputs]
    ].mul(num_attn_2_2_outputs, axis=0)

    # num_attn_2_3 ####################################################
    def num_predicate_2_3(mlp_0_1_output, attn_0_6_output):
        if mlp_0_1_output in {0, 9}:
            return attn_0_6_output == "</s>"
        elif mlp_0_1_output in {1, 13, 14}:
            return attn_0_6_output == "1"
        elif mlp_0_1_output in {2, 3, 4, 5, 6, 7, 10, 11, 12, 15}:
            return attn_0_6_output == "0"
        elif mlp_0_1_output in {8}:
            return attn_0_6_output == "<pad>"

    num_attn_2_3_pattern = select(attn_0_6_outputs, mlp_0_1_outputs, num_predicate_2_3)
    num_attn_2_3_outputs = aggregate_sum(num_attn_2_3_pattern, num_attn_1_6_outputs)
    num_attn_2_3_output_scores = classifier_weights.loc[
        [("num_attn_2_3_outputs", "_") for v in num_attn_2_3_outputs]
    ].mul(num_attn_2_3_outputs, axis=0)

    # num_attn_2_4 ####################################################
    def num_predicate_2_4(attn_1_3_output, token):
        if attn_1_3_output in {
            "6",
            "7",
            "1",
            "10",
            "0",
            "</s>",
            "<s>",
            "4",
            "3",
            "5",
            "8",
            "9",
        }:
            return token == "12"
        elif attn_1_3_output in {"11"}:
            return token == "11"
        elif attn_1_3_output in {"12"}:
            return token == "1"
        elif attn_1_3_output in {"2"}:
            return token == "2"

    num_attn_2_4_pattern = select(tokens, attn_1_3_outputs, num_predicate_2_4)
    num_attn_2_4_outputs = aggregate_sum(num_attn_2_4_pattern, num_attn_0_2_outputs)
    num_attn_2_4_output_scores = classifier_weights.loc[
        [("num_attn_2_4_outputs", "_") for v in num_attn_2_4_outputs]
    ].mul(num_attn_2_4_outputs, axis=0)

    # num_attn_2_5 ####################################################
    def num_predicate_2_5(q_mlp_0_1_output, k_mlp_0_1_output):
        if q_mlp_0_1_output in {0, 2, 3, 4, 5, 9, 11, 14}:
            return k_mlp_0_1_output == 8
        elif q_mlp_0_1_output in {1, 6, 7, 10, 15}:
            return k_mlp_0_1_output == 3
        elif q_mlp_0_1_output in {8}:
            return k_mlp_0_1_output == 6
        elif q_mlp_0_1_output in {12}:
            return k_mlp_0_1_output == 7
        elif q_mlp_0_1_output in {13}:
            return k_mlp_0_1_output == 2

    num_attn_2_5_pattern = select(mlp_0_1_outputs, mlp_0_1_outputs, num_predicate_2_5)
    num_attn_2_5_outputs = aggregate_sum(num_attn_2_5_pattern, num_attn_0_1_outputs)
    num_attn_2_5_output_scores = classifier_weights.loc[
        [("num_attn_2_5_outputs", "_") for v in num_attn_2_5_outputs]
    ].mul(num_attn_2_5_outputs, axis=0)

    # num_attn_2_6 ####################################################
    def num_predicate_2_6(attn_0_7_output, token):
        if attn_0_7_output in {
            "6",
            "7",
            "1",
            "12",
            "10",
            "0",
            "</s>",
            "<s>",
            "3",
            "5",
            "8",
            "11",
            "9",
        }:
            return token == "2"
        elif attn_0_7_output in {"2"}:
            return token == "12"
        elif attn_0_7_output in {"4"}:
            return token == "4"

    num_attn_2_6_pattern = select(tokens, attn_0_7_outputs, num_predicate_2_6)
    num_attn_2_6_outputs = aggregate_sum(num_attn_2_6_pattern, num_attn_0_1_outputs)
    num_attn_2_6_output_scores = classifier_weights.loc[
        [("num_attn_2_6_outputs", "_") for v in num_attn_2_6_outputs]
    ].mul(num_attn_2_6_outputs, axis=0)

    # num_attn_2_7 ####################################################
    def num_predicate_2_7(attn_1_6_output, attn_1_5_output):
        if attn_1_6_output in {"7", "5", "0", "</s>", "9"}:
            return attn_1_5_output == "4"
        elif attn_1_6_output in {"6", "1", "12", "10", "4", "11"}:
            return attn_1_5_output == "2"
        elif attn_1_6_output in {"2", "8"}:
            return attn_1_5_output == "5"
        elif attn_1_6_output in {"3"}:
            return attn_1_5_output == "3"
        elif attn_1_6_output in {"<s>"}:
            return attn_1_5_output == "11"

    num_attn_2_7_pattern = select(attn_1_5_outputs, attn_1_6_outputs, num_predicate_2_7)
    num_attn_2_7_outputs = aggregate_sum(num_attn_2_7_pattern, num_attn_0_1_outputs)
    num_attn_2_7_output_scores = classifier_weights.loc[
        [("num_attn_2_7_outputs", "_") for v in num_attn_2_7_outputs]
    ].mul(num_attn_2_7_outputs, axis=0)

    # mlp_2_0 #####################################################
    def mlp_2_0(attn_2_2_output, attn_2_6_output):
        key = (attn_2_2_output, attn_2_6_output)
        if key in {
            ("11", "0"),
            ("11", "1"),
            ("11", "10"),
            ("11", "11"),
            ("11", "12"),
            ("11", "3"),
            ("11", "7"),
            ("11", "8"),
            ("11", "<s>"),
            ("12", "0"),
            ("12", "1"),
            ("12", "10"),
            ("12", "11"),
            ("12", "12"),
            ("12", "3"),
            ("12", "7"),
            ("12", "8"),
            ("12", "<s>"),
            ("2", "0"),
            ("2", "1"),
            ("2", "10"),
            ("2", "11"),
            ("2", "12"),
            ("2", "3"),
            ("2", "7"),
            ("2", "8"),
            ("2", "<s>"),
            ("3", "0"),
            ("3", "1"),
            ("3", "10"),
            ("3", "11"),
            ("3", "12"),
            ("3", "3"),
            ("3", "7"),
            ("3", "8"),
            ("3", "<s>"),
            ("5", "0"),
            ("5", "1"),
            ("5", "10"),
            ("5", "11"),
            ("5", "12"),
            ("5", "3"),
            ("5", "7"),
            ("5", "8"),
            ("5", "<s>"),
            ("7", "0"),
            ("7", "1"),
            ("7", "10"),
            ("7", "11"),
            ("7", "12"),
            ("7", "3"),
            ("7", "7"),
            ("7", "8"),
            ("7", "<s>"),
            ("9", "0"),
            ("9", "1"),
            ("9", "10"),
            ("9", "11"),
            ("9", "12"),
            ("9", "3"),
            ("9", "4"),
            ("9", "7"),
            ("9", "8"),
            ("9", "9"),
            ("9", "</s>"),
            ("9", "<s>"),
            ("</s>", "0"),
            ("</s>", "1"),
            ("</s>", "10"),
            ("</s>", "11"),
            ("</s>", "12"),
            ("</s>", "3"),
            ("</s>", "7"),
            ("</s>", "8"),
            ("</s>", "<s>"),
        }:
            return 1
        elif key in {("8", "8")}:
            return 3
        return 15

    mlp_2_0_outputs = [
        mlp_2_0(k0, k1) for k0, k1 in zip(attn_2_2_outputs, attn_2_6_outputs)
    ]
    mlp_2_0_output_scores = classifier_weights.loc[
        [("mlp_2_0_outputs", str(v)) for v in mlp_2_0_outputs]
    ]

    # mlp_2_1 #####################################################
    def mlp_2_1(attn_2_5_output, position):
        key = (attn_2_5_output, position)
        if key in {
            ("0", 0),
            ("0", 3),
            ("0", 4),
            ("0", 5),
            ("0", 6),
            ("0", 7),
            ("0", 8),
            ("0", 9),
            ("0", 10),
            ("0", 11),
            ("0", 12),
            ("0", 14),
            ("0", 15),
            ("1", 0),
            ("1", 3),
            ("1", 4),
            ("1", 5),
            ("1", 6),
            ("1", 7),
            ("1", 8),
            ("1", 9),
            ("1", 10),
            ("1", 11),
            ("1", 12),
            ("1", 14),
            ("1", 15),
            ("10", 3),
            ("10", 4),
            ("10", 5),
            ("10", 6),
            ("10", 9),
            ("10", 11),
            ("10", 12),
            ("11", 5),
            ("11", 11),
            ("11", 12),
            ("11", 14),
            ("<s>", 1),
        }:
            return 15
        elif key in {
            ("0", 2),
            ("1", 2),
            ("10", 0),
            ("10", 2),
            ("10", 7),
            ("10", 8),
            ("10", 10),
            ("10", 15),
            ("11", 2),
            ("11", 7),
            ("11", 8),
            ("11", 10),
            ("12", 2),
            ("12", 10),
            ("2", 0),
            ("2", 2),
            ("2", 3),
            ("2", 4),
            ("2", 5),
            ("2", 6),
            ("2", 7),
            ("2", 8),
            ("2", 9),
            ("2", 10),
            ("2", 11),
            ("2", 12),
            ("2", 15),
        }:
            return 12
        elif key in {
            ("0", 1),
            ("1", 1),
            ("10", 1),
            ("11", 0),
            ("11", 1),
            ("11", 3),
            ("11", 4),
            ("11", 6),
            ("11", 9),
            ("11", 15),
            ("12", 1),
            ("2", 1),
            ("3", 1),
            ("4", 1),
            ("5", 1),
            ("6", 1),
            ("7", 1),
            ("8", 1),
            ("9", 1),
            ("</s>", 1),
        }:
            return 14
        return 7

    mlp_2_1_outputs = [mlp_2_1(k0, k1) for k0, k1 in zip(attn_2_5_outputs, positions)]
    mlp_2_1_output_scores = classifier_weights.loc[
        [("mlp_2_1_outputs", str(v)) for v in mlp_2_1_outputs]
    ]

    # mlp_2_2 #####################################################
    def mlp_2_2(position, attn_2_6_output):
        key = (position, attn_2_6_output)
        if key in {
            (0, "1"),
            (0, "10"),
            (1, "1"),
            (1, "10"),
            (1, "11"),
            (2, "11"),
            (2, "4"),
            (3, "1"),
            (3, "10"),
            (3, "12"),
            (3, "2"),
            (3, "4"),
            (3, "6"),
            (4, "0"),
            (4, "1"),
            (4, "10"),
            (4, "<s>"),
            (5, "1"),
            (5, "10"),
            (8, "1"),
            (8, "10"),
            (8, "11"),
            (8, "12"),
            (8, "2"),
            (8, "4"),
            (8, "6"),
            (8, "9"),
            (10, "0"),
            (10, "1"),
            (10, "10"),
            (10, "11"),
            (10, "12"),
            (10, "2"),
            (10, "3"),
            (10, "4"),
            (10, "5"),
            (10, "6"),
            (10, "7"),
            (10, "8"),
            (10, "9"),
            (10, "</s>"),
            (10, "<s>"),
            (11, "1"),
            (11, "10"),
            (12, "1"),
            (12, "10"),
            (13, "1"),
            (13, "10"),
            (15, "1"),
            (15, "10"),
        }:
            return 11
        elif key in {
            (0, "0"),
            (0, "<s>"),
            (1, "0"),
            (2, "0"),
            (2, "1"),
            (2, "10"),
            (2, "12"),
            (2, "2"),
            (2, "3"),
            (2, "5"),
            (2, "6"),
            (2, "7"),
            (2, "8"),
            (2, "9"),
            (2, "</s>"),
            (2, "<s>"),
            (3, "0"),
            (3, "<s>"),
            (5, "0"),
            (5, "<s>"),
            (6, "0"),
            (6, "1"),
            (6, "10"),
            (6, "<s>"),
            (8, "0"),
            (8, "5"),
            (8, "7"),
            (8, "8"),
            (8, "</s>"),
            (8, "<s>"),
            (11, "0"),
            (11, "5"),
            (11, "8"),
            (11, "<s>"),
            (12, "0"),
            (13, "0"),
            (14, "0"),
            (14, "1"),
            (14, "10"),
            (15, "0"),
        }:
            return 2
        elif key in {
            (1, "12"),
            (1, "2"),
            (1, "3"),
            (1, "4"),
            (1, "5"),
            (1, "6"),
            (1, "7"),
            (1, "8"),
            (1, "9"),
            (1, "</s>"),
            (1, "<s>"),
            (15, "<s>"),
        }:
            return 3
        return 10

    mlp_2_2_outputs = [mlp_2_2(k0, k1) for k0, k1 in zip(positions, attn_2_6_outputs)]
    mlp_2_2_output_scores = classifier_weights.loc[
        [("mlp_2_2_outputs", str(v)) for v in mlp_2_2_outputs]
    ]

    # mlp_2_3 #####################################################
    def mlp_2_3(position, attn_2_7_output):
        key = (position, attn_2_7_output)
        if key in {
            (0, "11"),
            (0, "12"),
            (0, "2"),
            (0, "4"),
            (0, "5"),
            (2, "6"),
            (2, "7"),
            (2, "8"),
            (2, "9"),
            (3, "0"),
            (3, "1"),
            (3, "11"),
            (3, "12"),
            (3, "2"),
            (3, "3"),
            (3, "4"),
            (3, "5"),
            (3, "6"),
            (3, "7"),
            (3, "8"),
            (3, "</s>"),
            (3, "<s>"),
            (4, "11"),
            (4, "12"),
            (4, "2"),
            (4, "4"),
            (4, "5"),
            (5, "11"),
            (5, "12"),
            (5, "2"),
            (5, "4"),
            (5, "5"),
            (5, "6"),
            (5, "7"),
            (5, "8"),
            (5, "9"),
            (6, "11"),
            (6, "12"),
            (6, "2"),
            (6, "4"),
            (6, "5"),
            (6, "6"),
            (6, "7"),
            (6, "8"),
            (7, "11"),
            (7, "2"),
            (7, "4"),
            (8, "11"),
            (8, "2"),
            (8, "4"),
            (9, "0"),
            (9, "1"),
            (9, "11"),
            (9, "12"),
            (9, "2"),
            (9, "4"),
            (9, "5"),
            (9, "</s>"),
            (9, "<s>"),
            (10, "11"),
            (10, "12"),
            (10, "2"),
            (10, "4"),
            (10, "5"),
            (10, "6"),
            (10, "7"),
            (10, "8"),
            (10, "9"),
            (10, "<s>"),
            (11, "11"),
            (11, "12"),
            (11, "2"),
            (11, "4"),
            (11, "5"),
            (12, "11"),
            (12, "2"),
            (12, "4"),
            (13, "11"),
            (13, "2"),
            (13, "4"),
            (15, "11"),
            (15, "12"),
            (15, "2"),
            (15, "4"),
            (15, "5"),
        }:
            return 7
        elif key in {
            (0, "6"),
            (0, "7"),
            (0, "8"),
            (0, "9"),
            (3, "9"),
            (4, "6"),
            (4, "7"),
            (4, "8"),
            (4, "9"),
            (6, "9"),
            (7, "12"),
            (7, "5"),
            (7, "6"),
            (7, "7"),
            (7, "8"),
            (7, "9"),
            (8, "12"),
            (8, "5"),
            (8, "6"),
            (8, "7"),
            (8, "8"),
            (8, "9"),
            (9, "3"),
            (9, "6"),
            (9, "7"),
            (9, "8"),
            (9, "9"),
            (11, "6"),
            (11, "7"),
            (11, "8"),
            (11, "9"),
            (12, "12"),
            (12, "5"),
            (12, "6"),
            (12, "7"),
            (12, "8"),
            (12, "9"),
            (13, "12"),
            (13, "5"),
            (13, "6"),
            (13, "7"),
            (13, "8"),
            (13, "9"),
            (14, "11"),
            (14, "12"),
            (14, "2"),
            (14, "3"),
            (14, "4"),
            (14, "5"),
            (14, "6"),
            (14, "7"),
            (14, "8"),
            (14, "9"),
            (14, "</s>"),
            (14, "<s>"),
            (15, "6"),
            (15, "7"),
            (15, "8"),
            (15, "9"),
        }:
            return 13
        elif key in {(4, "<s>"), (5, "<s>"), (10, "0"), (10, "3"), (15, "<s>")}:
            return 10
        elif key in {(14, "1")}:
            return 15
        return 6

    mlp_2_3_outputs = [mlp_2_3(k0, k1) for k0, k1 in zip(positions, attn_2_7_outputs)]
    mlp_2_3_output_scores = classifier_weights.loc[
        [("mlp_2_3_outputs", str(v)) for v in mlp_2_3_outputs]
    ]

    # num_mlp_2_0 #################################################
    def num_mlp_2_0(num_attn_0_3_output):
        key = num_attn_0_3_output
        return 10

    num_mlp_2_0_outputs = [num_mlp_2_0(k0) for k0 in num_attn_0_3_outputs]
    num_mlp_2_0_output_scores = classifier_weights.loc[
        [("num_mlp_2_0_outputs", str(v)) for v in num_mlp_2_0_outputs]
    ]

    # num_mlp_2_1 #################################################
    def num_mlp_2_1(num_attn_0_3_output):
        key = num_attn_0_3_output
        if key in {0}:
            return 0
        return 11

    num_mlp_2_1_outputs = [num_mlp_2_1(k0) for k0 in num_attn_0_3_outputs]
    num_mlp_2_1_output_scores = classifier_weights.loc[
        [("num_mlp_2_1_outputs", str(v)) for v in num_mlp_2_1_outputs]
    ]

    # num_mlp_2_2 #################################################
    def num_mlp_2_2(num_attn_0_7_output):
        key = num_attn_0_7_output
        if key in {0}:
            return 5
        return 15

    num_mlp_2_2_outputs = [num_mlp_2_2(k0) for k0 in num_attn_0_7_outputs]
    num_mlp_2_2_output_scores = classifier_weights.loc[
        [("num_mlp_2_2_outputs", str(v)) for v in num_mlp_2_2_outputs]
    ]

    # num_mlp_2_3 #################################################
    def num_mlp_2_3(num_attn_1_7_output, num_attn_1_0_output):
        key = (num_attn_1_7_output, num_attn_1_0_output)
        return 7

    num_mlp_2_3_outputs = [
        num_mlp_2_3(k0, k1)
        for k0, k1 in zip(num_attn_1_7_outputs, num_attn_1_0_outputs)
    ]
    num_mlp_2_3_output_scores = classifier_weights.loc[
        [("num_mlp_2_3_outputs", str(v)) for v in num_mlp_2_3_outputs]
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
                mlp_0_2_output_scores,
                mlp_0_3_output_scores,
                num_mlp_0_0_output_scores,
                num_mlp_0_1_output_scores,
                num_mlp_0_2_output_scores,
                num_mlp_0_3_output_scores,
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
                mlp_1_2_output_scores,
                mlp_1_3_output_scores,
                num_mlp_1_0_output_scores,
                num_mlp_1_1_output_scores,
                num_mlp_1_2_output_scores,
                num_mlp_1_3_output_scores,
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
                mlp_2_2_output_scores,
                mlp_2_3_output_scores,
                num_mlp_2_0_output_scores,
                num_mlp_2_1_output_scores,
                num_mlp_2_2_output_scores,
                num_mlp_2_3_output_scores,
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


print(run(["<s>", "3", "3", "2", "4", "</s>"]))
