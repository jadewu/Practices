# Only adjacent non-repeative letters in the 2d array can construct words
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(board, i, j, word):
            # finish checking all words
            if len(word) == 0:
                return True
            # check whether i,j out of range and the first letter is at (i,j)
            if (i<0) or (i>len(board)-1) or (j<0) or (j>len(board[0])-1) or (word[0] != board[i][j]):
                return False
            
            temp = board[i][j]
            # avoid revisit 
            board[i][j] = "#"
            
            # check whether the next word is adjacent
            nword = word[1:]
            res = dfs(board,i+1,j,nword) or dfs(board,i,j+1,nword) or dfs(board,i-1,j,nword) or dfs(board,i,j-1,nword)
            # restore the array after one dfs search
            board[i][j] = temp
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False
    
        
