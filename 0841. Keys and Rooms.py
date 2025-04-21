class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(root):
            visited.add(root)
            for child in rooms[root]:
                if child not in visited:
                    dfs(child)
        dfs(0)
        return len(visited) == len(rooms)
