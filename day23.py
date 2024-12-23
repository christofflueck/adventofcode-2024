from collections import defaultdict
from run_util import run_puzzle


def parse_data(data: str):
    links = [tuple(sorted(x.split("-"))) for x in data.splitlines()]

    lookup = defaultdict(set)
    for left, right in links:
        lookup[left].add(right)
        lookup[right].add(left)

    return links, lookup


def part_a(data: str) -> int:
    links, lookup = parse_data(data)

    networks = set()

    for left, right in links:
        for node in lookup:
            if left in lookup[node] and right in lookup[node]:
                networks.add(tuple(sorted([left, right, node])))

    return len(
        [
            1
            for n1, n2, n3 in networks
            if n1.startswith("t") or n2.startswith("t") or n3.startswith("t")
        ]
    )


# source: https://github.com/alanmc-zz/python-bors-kerbosch/blob/master/bors-kerbosch.py
def bors_kerbosch(R, P, X, G, C):
    if len(P) == 0 and len(X) == 0:
        if len(R) > 2:
            C.append(sorted(R))            
        return

    (d, pivot) = max([(len(G[v]), v) for v in P.union(X)])
                     
    for v in P.difference(G[pivot]):
        bors_kerbosch(R.union(set([v])), P.intersection(G[v]), X.intersection(G[v]), G, C)
        P.remove(v)
        X.add(v)


def part_b(data: str) -> int:
    _, lookup = parse_data(data)
    C1 = []
    bors_kerbosch(set([]), set(lookup.keys()), set([]), lookup, C1)

    return ",".join(sorted(max(C1, key=len)))


def main():
    examples = [
        (
            """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""",
            7,
            "co,de,ka,ta",
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
