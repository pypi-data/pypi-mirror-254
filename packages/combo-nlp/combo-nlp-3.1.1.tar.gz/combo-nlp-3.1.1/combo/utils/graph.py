"""Based on https://github.com/emorynlp/iwpt-shared-task-2020."""

import numpy as np

_ACL_REL_CL = "acl:relcl"


def graph_and_tree_merge(tree_arc_scores,
                         tree_rel_scores,
                         graph_arc_scores,
                         graph_rel_scores,
                         label2idx,
                         idx2label,
                         graph_label2idx,
                         graph_idx2label,
                         tokens):
    graph_arc_scores = np.copy(graph_arc_scores)
    # Exclude self-loops, in-place operation.
    np.fill_diagonal(graph_arc_scores, 0)
    # Connection to root will be handled by tree.
    graph_arc_scores[:, 0] = False
    # The same with labels.
    root_idx = graph_label2idx["root"]
    graph_rel_scores[:, :, root_idx] = -float('inf')
    graph_rel_pred = graph_rel_scores.argmax(-1)

    # Add tree edges to graph
    tree_heads = [0] + tree_arc_scores
    graph = [[] for _ in range(len(tree_heads))]
    labeled_graph = [[] for _ in range(len(tree_heads))]
    for d, h in enumerate(tree_heads):
        if not d:
            continue
        label = idx2label[tree_rel_scores[d - 1]]
        # graph_label = graph_idx2label[graph_rel_pred[d - 1][h - 1]]
        # if ">" in graph_label and label in graph_label:
        #     print("Using graph label instead of tree.")
        #     label = graph_label
        if label != _ACL_REL_CL:
            graph[h].append(d)
            labeled_graph[h].append((d, label))

    # Debug only
    # Extract graph edges
    graph_edges = np.argwhere(graph_arc_scores)

    # Add graph edges which aren't creating a cycle
    for (d, h) in graph_edges:
        if not d or not h or d in graph[h]:
            continue
        try:
            path = next(_dfs(graph, d, h))
        except StopIteration:
            # There is not path from d to h
            label = graph_idx2label[graph_rel_pred[d][h]]
            if label != _ACL_REL_CL:
                graph[h].append(d)
                labeled_graph[h].append((d, label))

    # Add 'acl:relcl' without checking for cycles.
    for d, h in enumerate(tree_heads):
        if not d:
            continue
        label = idx2label[tree_rel_scores[d - 1]]
        if label == _ACL_REL_CL:
            graph[h].append(d)
            labeled_graph[h].append((d, label))

    assert len(labeled_graph[0]) == 1
    d = graph[0][0]
    graph[d].append(0)
    labeled_graph[d].append((0, "root"))

    parse_graph = [[] for _ in range(len(tree_heads))]
    for h in range(len(tree_heads)):
        for d, label in labeled_graph[h]:
            parse_graph[d].append((h, label))
        parse_graph[d] = sorted(parse_graph[d])

    for i, g in enumerate(parse_graph):
        heads = np.array([x[0] for x in g])
        rels = np.array([x[1] for x in g])
        indices = rels.argsort()
        heads = heads[indices].tolist()
        rels = rels[indices].tolist()
        deps = '|'.join(f'{h}:{r}' for h, r in zip(heads, rels))
        tokens[i - 1]["deps"] = deps
    return


def _dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path + [next_state]))


def restore_collapse_edges(tree_tokens):
    # https://gist.github.com/hankcs/776e7d95c19e5ff5da8469fe4e9ab050
    empty_tokens = []
    for token in tree_tokens:
        deps = token["deps"].split("|")
        for i, d in enumerate(deps):
            if ">" in d:
                # {head}:{empty_node_relation}>{current_node_relation}
                # should map to
                # For new, empty node:
                # {head}:{empty_node_relation}
                # For current node:
                # {new_empty_node_id}:{current_node_relation}
                # TODO consider where to put new_empty_node_id (currently at the end)
                head, relation = d.split(':', 1)
                ehead = f"{len(tree_tokens)}.{len(empty_tokens) + 1}"
                empty_node_relation, current_node_relation = relation.split(">", 1)
                # Edge case, double >
                if ">" in current_node_relation:
                    second_empty_node_relation, current_node_relation = current_node_relation.split(">")
                    deps[i] = f"{ehead}:{current_node_relation}"
                    second_ehead = f"{len(tree_tokens)}.{len(empty_tokens) + 2}"
                    empty_tokens.append(
                        {
                            "idx": ehead,
                            "deps": f"{second_ehead}:{empty_node_relation}"
                        }
                    )
                    empty_tokens.append(
                        {
                            "idx": second_ehead,
                            "deps": f"{head}:{second_empty_node_relation}"
                        }
                    )

                else:
                    deps[i] = f"{ehead}:{current_node_relation}"
                    empty_tokens.append(
                        {
                            "idx": ehead,
                            "deps": f"{head}:{empty_node_relation}"
                        }
                    )
        deps = sorted([d.split(":", 1) for d in deps], key=lambda x: float(x[0]))
        token["deps"] = "|".join([f"{k}:{v}" for k, v in deps])
    return empty_tokens
