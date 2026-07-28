/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public int MaxDepth(TreeNode root) 
    //{
        // return 0 if null
    //     if (root == null)
    //         return 0;

    //     return 1 + Math.Max(MaxDepth(root.left), MaxDepth(root.right));     
    // }

    // public int MaxDepthIterative(TreeNode root) 
    {
        // use a queue and then process the queue

        if (root == null)
            return 0;

        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        var depth = 0;

        while (queue.Count > 0)
        {
            int levelCount = queue.Count; // nodes at this level
            depth++;

            for (var i = 0; i < levelCount; i++)
            {
                TreeNode cur = queue.Dequeue();
                if (cur.left != null)
                {
                    queue.Enqueue(cur.left);
                }
                if (cur.right != null)
                {
                    queue.Enqueue(cur.right);
                }
            }
        }

        return depth;
    }
}
