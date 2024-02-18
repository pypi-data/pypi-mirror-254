from collections import defaultdict
from typing import Generator, List

from ragraph.edge import Edge
from ragraph.graph import Graph
from ragraph.node import Node

import raesl.doc.lines as lns
from raesl.doc import utils

LineGen = Generator[str, None, None]


def get_comp_node_html_table(node: Node, graph: Graph, node_kinds: List[str]) -> LineGen:
    """Returns a HTML grid table."""
    yield lns.boldhead(lns.node_path(node.name), html=True)
    yield "<br>"
    yield "<hr>"
    if node.children:
        yield lns.boldhead("sub-components:")
        yield "<br>"
        yield from lns.unordered([lns.node_path(c.name) for c in node.children], html=True)
    props = utils.get_component_properties(node, graph)
    if props:
        yield lns.boldhead("properties:")
        yield "<br>"
        yield from lns.unordered([lns.node_path(p.name) for p in props], html=True)
    yield "<br>"

    plain_comments = (
        [("comments", node.annotations.esl_info.get("comments", []))]
        if node.annotations.esl_info.get("comments", [])
        else []
    )

    tagged_comments = list(node.annotations.esl_info["tagged_comments"].items())

    if plain_comments or tagged_comments:
        for key, comments in plain_comments + tagged_comments:
            yield lns.boldhead(key, html=True)
            yield "<br>"
            yield " ".join(comments)
            yield "<br><br>"

    related_nodes_by_kind = defaultdict(list)
    for n in [
        e.target
        for e in graph.edges_from(node)
        if e.kind == "mapping_dependency" and e.target.kind in node_kinds
    ]:
        if n.kind == "function_spec":
            related_nodes_by_kind[n.annotations.esl_info["sub_kind"]].append(n)
        else:
            related_nodes_by_kind[n.kind].append(n)

    if "function_spec" in node_kinds:
        if related_nodes_by_kind.get("goal"):
            yield lns.boldhead("goal function specifications", html=True)
            yield "<br>"
            yield "<hr>"
            yield "<br>"
            for g in related_nodes_by_kind.get("goal") or []:
                yield from get_spec_node_html_text(node=g, graph=graph)

        if related_nodes_by_kind.get("transformation"):
            yield lns.boldhead("Transformation function specifications", html=True)
            yield "<br>"
            yield "<hr>"
            yield "<br>"
            for t in related_nodes_by_kind.get("transformation") or []:
                yield from get_spec_node_html_text(node=t, graph=graph)

    if "behavior_spec" in node_kinds:
        if related_nodes_by_kind.get("behavior_spec", None):
            yield lns.boldhead("behavior specifications", html=True)
            yield "<br>"
            yield "<hr>"
            yield "<br>"
            for g in related_nodes_by_kind.get("behavior_spec") or []:
                yield from get_spec_node_html_text(node=g, graph=graph)

    if "design_spec" in node_kinds:
        if related_nodes_by_kind.get("design_spec", None):
            yield lns.boldhead("design specifications", html=True)
            yield "<br>"
            yield "<hr>"
            yield "<br>"
            for g in related_nodes_by_kind.get("design_spec") or []:
                yield from get_spec_node_html_text(node=g, graph=graph)

    if "need" in node_kinds:
        if related_nodes_by_kind.get("need", None):
            yield lns.boldhead("needs", html=True)
            yield "<br>"
            yield "<hr>"
            yield "<br>"
            for g in related_nodes_by_kind.get("need") or []:
                yield from get_spec_node_html_text(node=g, graph=graph)

    if "relation_spec" in node_kinds:
        if related_nodes_by_kind.get("relation_spec", None):
            yield lns.boldhead("Relations specifications", html=True)
            yield "<br>"
            yield "<hr>"
            yield "<br>"
            for r in related_nodes_by_kind.get("relation_spec") or []:
                yield from relation_node_html_table(r=r, g=graph)


def get_spec_node_html_text(node: Node, graph: Graph) -> LineGen:
    """Yields ESL info belonging to spec node in html format."""
    yield lns.boldhead(lns.node_path(node.name), html=True)
    yield "<br>"
    yield "<hr>"
    yield from lns.lines(node, graph=graph, html=True)
    yield "<br>"

    sub_nodes = None
    if node.kind == "function_spec":
        if node.annotations.esl_info["sub_kind"]:
            sub_nodes = [
                e.target
                for e in graph.edges
                if e.source is node and e.kind == "traceability_dependency"
            ]

    if sub_nodes:
        yield lns.boldhead("subordinate function specifications:", html=True)
        yield "<hr>"
        yield from lns.unordered([lns.node_path(s.name) for s in sub_nodes], html=True)
        yield "<br>"

    plain_comments = (
        [("comments", node.annotations.esl_info.get("comments", []))]
        if node.annotations.esl_info.get("comments", [])
        else []
    )

    tagged_comments = list(node.annotations.esl_info["tagged_comments"].items())

    if plain_comments or tagged_comments:
        for key, comments in plain_comments + tagged_comments:
            yield lns.boldhead(key, html=True)
            yield "<br>"
            yield " ".join(comments)
            yield "<br>"

    yield "<hr>"
    yield "<br>"


def get_edge_html_text(edge: Edge, graph: Graph) -> LineGen:
    """Yields ESL info belonging to an edge."""
    if not edge.annotations.get("esl_info", None):
        yield ""
    elif edge.annotations.esl_info["reason"].get("function_specifications", None):
        yield lns.boldhead("Function specifications", html=True)
        yield "<br>"
        yield "<hr>"
        yield "<br>"
        for fname in edge.annotations.esl_info["reason"]["function_specifications"]:
            yield from get_spec_node_html_text(node=graph[fname], graph=graph)

    elif edge.annotations.esl_info["reason"].get("design_specifications", None):
        yield lns.boldhead("Design specifications", html=True)
        yield "<br>"
        yield "<hr>"
        yield "<br>"
        for dname in edge.annotations.esl_info["reason"]["design_specifications"]:
            yield from get_spec_node_html_text(node=graph[dname], graph=graph)

    elif edge.annotations.esl_info["reason"].get("relation_specifications", None):
        yield lns.boldhead("Relation specifications", html=True)
        yield "<br>"
        yield "<hr>"
        yield "<br>"
        for rname in edge.annotations.esl_info["reason"]["relation_specifications"]:
            yield from relation_node_html_table(r=graph[rname], g=graph)

    elif edge.annotations.esl_info["reason"].get("behavior_specifications", None):
        yield lns.boldhead("Behavior specifications", html=True)
        yield "<br>"
        yield "<hr>"
        yield "<br>"
        for bname in edge.annotations.esl_info["reason"]["behavior_specifications"]:
            yield from get_spec_node_html_text(node=graph[bname], graph=graph)
    elif edge.annotations.esl_info["reason"].get("shared_variables", None):
        yield lns.boldhead("Shared variables", html=True)
        yield "<br>"
        yield "<hr>"
        yield "<br>"
        for vname in edge.annotations.esl_info["reason"]["shared_variables"]:
            yield lns.node_path(vname)
            yield "<br>"
        yield "<br>"
    else:
        yield ""


def relation_node_html_table(r: Node, g: Graph) -> LineGen:
    ri = r.annotations.esl_info
    yield lns.bold(lns.node_path(r.name), html=True)
    yield "<br>"
    yield "<hr>"
    yield lns.bold("model definition name:", html=True)
    yield "<br>"
    yield ri["definition_name"].replace("\n", "")
    yield "<br>"
    yield "<hr>"
    if ri.get("required_variables"):
        yield lns.bold("required variables:", html=True)
        yield "<br>"
        yield from lns.unordered(
            [lns.var_path(g[v]).replace("\n", "") for v in ri.get("required_variables")],
            html=True,
        )
    if ri.get("returned_variables"):
        yield lns.bold("returned variables:", html=True)
        yield "<br>"
        yield from lns.unordered(
            [lns.var_path(g[v]).replace("\n", "") for v in ri.get("returned_variables")],
            html=True,
        )
    if ri.get("related_variables"):
        yield lns.bold("related variables:", html=True)
        yield "<br>"
        yield from lns.unordered(
            [lns.var_path(g[v]).replace("\n", "") for v in ri.get("related_variables")],
            html=True,
        )
    yield "<br>"

    plain_comments = (
        [("comments", r.annotations.esl_info.get("comments", []))]
        if r.annotations.esl_info.get("comments", [])
        else []
    )

    tagged_comments = list(r.annotations.esl_info["tagged_comments"].items())

    if plain_comments or tagged_comments:
        for key, comments in plain_comments + tagged_comments:
            yield lns.boldhead(key, html=True)
            yield "<br>"
            yield " ".join(comments)
            yield "<br><br>"
