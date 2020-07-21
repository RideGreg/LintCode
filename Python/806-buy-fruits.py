# 806
# Xiao Ming is going to help companies buy fruit. Give a codeList, which is loaded with the
# fruit he bought. Give a shoppingCart, which is loaded with target fruit.
#
# We need to check if the order in the codeList matches the order in the shoppingCart.
# Note that only the sum of the items in all linked lists in the codeList add up to less than or
# equal to the sum of items in the shoppingcart may return 1.
#
# In addition, the item in codeList may be "anything", which can match with any fruit.

class Solution:
    """
    @param codeList: The codeList
    @param shoppingCart: The shoppingCart
    @return: The answer
    """
    def buyFruits(self, codeList, shoppingCart):
        sumCodeList = 0
        for itemList in codeList:
            sumCodeList += len(itemList)
        sumShoppingCart = len(shoppingCart)
        if sumCodeList > sumShoppingCart:
            return 0

        for i in range(sumShoppingCart - sumCodeList + 1):
            idx = 0
            for itemList in codeList:
                for j in itemList:
                    if j == shoppingCart[i + idx] or j == 'anything':
                        idx += 1
                    else:
                        idx = -1
                        break
                if idx == -1:
                    break
            if idx == sumCodeList:
                return 1
        return 0

print(Solution().buyFruits(
    [["apple", "apple"],["orange", "banana", "orange"]],
    ["orange", "apple", "apple", "orange", "banana", "orange"])) # 1
# Explanation: Because the order in the codeList matches the fruit in the shoppingCart
# except for the first orange.
print(Solution().buyFruits(
    [["orange", "banana", "orange"],["apple", "apple"]],
    ["orange", "apple", "apple", "orange", "banana", "orange"])) # 0
# Explanation: Because the order in the codeList doesn't match the shoppingCart.

print(Solution().buyFruits(
    [["apple", "apple"],["orange", "anything", "orange"]],
    ["orange", "apple", "apple", "orange", "mango", "orange"])) # 1
# Explanation: anything matches mango, so codeList can match the fruit of shoppingCart.