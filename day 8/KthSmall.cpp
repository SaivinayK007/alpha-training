
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };
class Solution {
public:
    int c = 0  ,s = 0;
    void inorder(TreeNode* root , int k){
        if(root){
            inorder(root->left, k);
            c++;
            if(c == k){
                s = root->val;
                return;
            }
            inorder(root->right, k);
        }
    }
    int kthSmallest(TreeNode* root, int k) {
        inorder(root , k);
        return s;
        
    }
};