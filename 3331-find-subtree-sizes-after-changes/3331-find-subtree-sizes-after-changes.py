class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        nearest = [{} for _ in range(n)]
        new_parent = [-1] * n

        def dfs(u, ancestors):
            ch = s[u]

            if ch in ancestors:
                new_parent[u] = ancestors[ch]
            else:
                new_parent[u] = parent[u]

            ancestors[ch] = u

            for v in children[u]:
                dfs(v, ancestors)

            ancestors[ch] = -1 if len(ancestors) == 0 else ancestors[ch]

        # Build the updated parent relationships.
        def build(u, path):
            ch = s[u]
            old = path.get(ch, -1)

            if old != -1:
                new_parent[u] = old
            else:
                new_parent[u] = parent[u]

            path[ch] = u

            for v in children[u]:
                build(v, path)

            if old == -1:
                del path[ch]
            else:
                path[ch] = old

        build(0, {})

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [1] * n

        def count(u):
            for v in new_children[u]:
                ans[u] += count(v)
            return ans[u]

        count(0)
        return ans