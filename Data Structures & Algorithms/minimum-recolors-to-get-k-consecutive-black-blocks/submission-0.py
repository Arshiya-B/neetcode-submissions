class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
    
        white_count = blocks[:k].count("W")
        min_recolor = white_count

        for r in range(k, len(blocks)):
            if blocks[r] == "W":
                white_count +=1
            
            left = r-k

            if blocks[left] == "W":
                white_count-=1

        
            min_recolor = min(white_count, min_recolor)
        
        return min_recolor
