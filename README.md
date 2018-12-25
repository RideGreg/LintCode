# [LintCode](http://www.lintcode.com/en/problem/) ![Language](https://img.shields.io/badge/language-C++%2011-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) ![Progress](https://img.shields.io/badge/progress-289%20%2F%20289-ff69b4.svg)

Up to date (2016-08-22), there are `289` problems on [LintCode Online Judge](http://lintcode.com/).
The number of problems is increasing recently.
Here is the classification of all `289` problems.
For more problems and solutions, you can see my [LeetCode](https://github.com/RideGreg/LeetCode) repository.
I'll keep updating for full summary and better solutions. Stay tuned for updates.

## Algorithms
* [Bit Manipulation](https://github.com/RideGreg/LintCode#bit-manipulation)
* [Array](https://github.com/RideGreg/LintCode#array)
* [String](https://github.com/RideGreg/LintCode#string)
* [Linked List](https://github.com/RideGreg/LintCode#linked-list)
* [Math](https://github.com/RideGreg/LintCode#math)
* [Tree](https://github.com/RideGreg/LintCode#tree)
* [Stack](https://github.com/RideGreg/LintCode#stack)
* [Queue](https://github.com/RideGreg/LintCode#queue)
* [Heap](https://github.com/RideGreg/LintCode#heap)
* [Hash Tables](https://github.com/RideGreg/LintCode#hash-tables)
* [Data Structure](https://github.com/RideGreg/LintCode#data-structure)
* [Sort](https://github.com/RideGreg/LintCode#sort)
* [Recursion](https://github.com/RideGreg/LintCode#recursion)
* [Binary Search](https://github.com/RideGreg/LintCode#binary-search)
* [Breadth-First Search](https://github.com/RideGreg/LintCode#breadth-first-search)
* [Depth-First Search](https://github.com/RideGreg/LintCode#depth-first-search)
* [Backtracking](https://github.com/RideGreg/LintCode#backtracking)
* [Binary Search Trees](https://github.com/RideGreg/LintCode#binary-search-trees)
* [Dynamic Programming](https://github.com/RideGreg/LintCode#dynamic-programming)
* [Greedy](https://github.com/RideGreg/LintCode#greedy)
* [OO Design](https://github.com/RideGreg/LintCode#oo-design)
* [System Design](https://github.com/RideGreg/LintCode#system-design)

## Bit Manipulation
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|1|[A + B Problem](http://lintcode.com/en/problem/a-b-problem/)| [C++](./C++/a-b-problem.cpp)| _O(1)_ | _O(1)_ | Medium | | |
|82|[Single Number](http://lintcode.com/en/problem/single-number/)| [C++](./C++/single-number.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode| |
|83|[Single Number II](http://lintcode.com/en/problem/single-number-ii/)| [C++](./C++/single-number-ii.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|84|[Single Number III](http://lintcode.com/en/problem/single-number-iii/)| [C++](./C++/single-number-iii.cpp) [Python](./Python/single-number-iii.py)| _O(n)_ | _O(1)_ | Medium | CTCI | |
|142|[O(1) Check Power of 2](http://lintcode.com/en/problem/o1-check-power-of-2/)| [C++](./C++/o1-check-power-of-2.cpp)| _O(1)_ | _O(1)_ | Easy | | |
|179|[Update Bits](http://lintcode.com/en/problem/update-bits/)| [C++](./C++/update-bits.cpp)| _O(1)_ | _O(1)_ | Medium | CTCI | |
|181|[Flip Bits](http://lintcode.com/en/problem/flip-bits/)| [C++](./C++/flip-bits.cpp)| _O(1)_ | _O(1)_ | Easy | CTCI | |
|196|[Find the Missing Number](http://lintcode.com/en/problem/find-the-missing-number/)| [C++](./C++/find-the-missing-number.cpp)| _O(n)_ | _O(1)_ | Medium | | |
|365|[Count 1 in Binary](http://lintcode.com/en/problem/count-1-in-binary/)| [C++](./C++/count-1-in-binary.cpp)| _O(1)_ | _O(1)_ | Easy | CTCI | |

## Array
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|6|[Merge Sorted Array](http://lintcode.com/en/problem/merge-sorted-array-ii/)| [Python](./Python/merge-sorted-array-ii.py) [C++](./C++/merge-sorted-array-ii.cpp) [Java](./Java/merge-sorted-array-ii.java)| _O(m + n)_ | _O(1)_ | Easy | LeetCode | Two Pointers |
|8|[Rotate String](http://lintcode.com/en/problem/rotate-string/)| [C++](./C++/rotate-string.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|9|[Fizz Buzz](http://lintcode.com/en/problem/fizz-buzz/)| [C++](./C++/fizz-buzz.cpp)| _O(n)_ | _O(1)_ | Easy | | |
|30|[Insert Interval](http://lintcode.com/en/problem/insert-interval/)| [C++](./C++/insert-interval.cpp) [Python](./Python/30-insert-interval.py) | _O(n)_ | _O(1)_ | Easy | LeetCode, EPI, Google Ladder 18/7 | |
|31|[Partition Array](http://lintcode.com/en/problem/partition-array/)| [C++](./C++/partition-array.cpp)| _O(n)_ | _O(1)_ | Medium | | Two Pointers |
|32|[Minimum Window Substring](http://lintcode.com/en/problem/minimum-window-substring/)| [C++](./C++/minimum-window-substring.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|38|[Search a 2D Matrix II](http://lintcode.com/en/problem/search-a-2d-matrix-ii/)| [C++](./C++/search-a-2d-matrix-ii.cpp)| _O(m + n)_ | _O(1)_ | Medium | EPI | |
|39|[Recover Rotated Sorted Array](http://lintcode.com/en/problem/recover-rotated-sorted-array/)| [C++](./C++/recover-rotated-sorted-array.cpp)| _O(n)_ | _O(1)_ | Easy | | |
|46|[Majority Number](http://lintcode.com/en/problem/majority-number/)| [C++](./C++/majority-number.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|47|[Majority Number II](http://lintcode.com/en/problem/majority-number/)| [C++](./C++/majority-number-ii.cpp)| _O(n)_ | _O(1)_ | Medium | EPI | |
|48|[Majority Number III](http://lintcode.com/en/problem/majority-number-iii/)| [C++](./C++/majority-number-iii.cpp)| _O(n)_ | _O(k)_ | Medium | EPI | |
|49|[Sort Letters by Case](http://lintcode.com/en/problem/sort-letters-by-case/)| [C++](./C++/sort-letters-by-case.cpp)| _O(n)_ | _O(1)_ | Medium | | Two Pointers |
|50|[Product of Array Exclude Itself](http://lintcode.com/en/problem/product-of-array-exclude-itself/)| [C++](./C++/product-of-array-exclude-itself.cpp)| _O(n)_ | _O(1)_ | Easy | | |
|51|[Previous Permutation](http://lintcode.com/en/problem/previous-permutation/)| [C++](./C++/previous-permutation.cpp)| _O(n)_ | _O(1)_ | Medium | | |
|52|[Next Permutation](http://lintcode.com/en/problem/next-permutation/)| [C++](./C++/next-permutation.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|57|[3 Sum](http://lintcode.com/en/problem/3-sum/)| [C++](./C++/3-sum.cpp)| _O(n^2)_ | _O(1)_ | Medium | LeetCode | Two Pointers, Sort |
|58|[4 Sum](http://lintcode.com/en/problem/4-sum/)| [C++](./C++/4-sum.cpp)| _O(n^3)_ | _O(1)_ | Medium | LeetCode | Hash |
|59|[3 Sum Closest](http://lintcode.com/en/problem/3-sum-closest/)| [C++](./C++/3-sum-closest.cpp)| _O(n^2)_ | _O(1)_ | Medium | LeetCode | Two Pointers, Sort |
|64|[Merge Sorted Array II](http://lintcode.com/en/problem/merge-sorted-array/)| [Python](./Python/merge-sorted-array.py) [C++](./C++/merge-sorted-array.cpp) | _O(m + n)_ | _O(1)_ | Easy | LeetCode | Two Pointers |
|100|[Remove Duplicates from Sorted Array](http://lintcode.com/en/problem/remove-duplicates-from-sorted-array/)| [C++](./C++/remove-duplicates-from-sorted-array.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | Two Pointers |
|101|[Remove Duplicates from Sorted Array II](http://lintcode.com/en/problem/remove-duplicates-from-sorted-array-ii/)| [C++](./C++/remove-duplicates-from-sorted-array-ii.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | Two Pointers |
|133|[Longest Words](http://lintcode.com/en/problem/longest-words/)| [C++](./C++/longest-words.cpp)| _O(n)_ | _O(n)_ | Easy | | |
|144|[Interleaving Positive and Negative Numbers](http://lintcode.com/en/problem/interleaving-positive-and-negative-numbers/)| [C++](./C++/interleaving-positive-and-negative-numbers.cpp)| _O(n)_ | _O(1)_ | Medium | | Two Pointers |
|161|[Rotate Image](http://lintcode.com/en/problem/rotate-image/)| [C++](./C++/rotate-image.cpp)| _O(n^2)_ | _O(1)_ | Medium | LeetCode | |
|162|[Set Matrix Zeroes](http://lintcode.com/en/problem/set-matrix-zeroes/)| [C++](./C++/set-matrix-zeroes.cpp)| _O(m * n)_ | _O(1)_ | Medium | LeetCode | |
|172|[Remove Element](http://lintcode.com/en/problem/remove-element/)| [C++](./C++/remove-element.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | Two Pointers |
|185|[Matrix Zigzag Traversal](http://lintcode.com/en/problem/matrix-zigzag-traversal/)| [C++](./C++/matrix-zigzag-traversal.cpp)| _O(m * n)_ | _O(1)_ | Easy | | |
|189|[First Missing Positive](http://lintcode.com/en/problem/first-missing-positive/)| [C++](./C++/first-missing-positive.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode, EPI | Hash |
|190|[Next Permutation II](http://lintcode.com/en/problem/next-permutation-ii/)| [C++](./C++/next-permutation-ii.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|200|[Longest Palindromic Substring](http://lintcode.com/en/problem/longest-palindromic-substring/)| [C++](./C++/longest-palindromic-substring.cpp)| _O(n)_ | _O(n)_ | Medium | LeetCode | `Manacher's Algorithm` |
|363|[Trapping Rain Water](http://lintcode.com/en/problem/trapping-rain-water/)| [C++](./C++/trapping-rain-water.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | Two Pointers, Tricky |
|373|[Partition Array by Odd and Even](http://lintcode.com/en/problem/partition-array-by-odd-and-even/)| [C++](./C++/partition-array-by-odd-and-even.cpp)| _O(n)_ | _O(1)_ | Easy | | Two Pointers |
|374| [Spiral Matrix](http://lintcode.com/en/problem/spiral-matrix/) | [C++](./C++/spiral-matrix.cpp) | _O(m * n)_    | _O(1)_         | Medium         | LeetCode | |
|381| [Spiral Matrix II](http://lintcode.com/en/problem/spiral-matrix-ii/) | [C++](./C++/spiral-matrix-ii.cpp) | _O(n^2)_ | _O(1)_      | Medium         | LeetCode | |
|382|[Triangle Count](http://lintcode.com/en/problem/triangle-count/)| [C++](./C++/triangle-count.cpp)| _O(n^2)_ | _O(1)_ | Medium | | Two Pointers |
|383|[Container With Most Water](http://lintcode.com/en/problem/container-with-most-water/)| [C++](./C++/container-with-most-water.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode, EPI | Two Pointers |
|388|[Permutation Sequence](http://lintcode.com/en/problem/permutation-sequence/)| [C++](./C++/permutation-sequence.cpp)| _O(n^2)_ | _O(n)_ | Medium | LeetCode | |
|389|[Valid Sudoku](http://lintcode.com/en/problem/valid-sudoku/)| [C++](./C++/valid-sudoku.cpp)| _O(9^2)_ | _O(9)_ | Easy | LeetCode | |
|404|[Subarray Sum II](http://lintcode.com/en/problem/subarray-sum-ii/)| [C++](./C++/subarray-sum-ii.cpp)| _O(nlogn)_ | _O(n)_ | Hard | | Two Pointers, Binary Search |
|405|[Submatrix Sum](http://lintcode.com/en/problem/submatrix-sum/)| [C++](./C++/submatrix-sum.cpp)| _O(m * n^2)_ | _O(m)_ | Hard | | Hash |
|406|[Minimum Size Subarray Sum](http://lintcode.com/en/problem/minimum-size-subarray-sum/)| [C++](./C++/minimum-size-subarray-sum.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | Two Pointers, Binary Search |
|539|[Move Zeroes](http://lintcode.com/en/problem/move-zeroes/)| [C++](./C++/move-zeroes.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | Two Pointers |
|817|[Range Sum Query 2D - Mutable](http://lintcode.com/en/problem/range-sum-query-2d-mutable/)| [Python](./Python/817-range-sum-query-2d-mutable.py)| _O(logMlogN) | _O(M*N)_ | Hard | Google Ladder 18/7 | Bit Indexed Tree, TLE Segment Tree |
|840|[Range Sum Query - Mutable](http://lintcode.com/en/problem/range-sum-query-mutable/)| [Python](./Python/840-range-sum-query-mutable.py)| _O(logn) | _O(n)_ | Medium | | Segment Tree |
|943|[Range Sum Query - Immutable](http://lintcode.com/en/problem/range-sum-query-immutable/)| [Python](./Python/943-range-sum-query-immutable.py)| _O(1) | _O(n)_ | Easy | | prefixSum |
|1539|[Flipped The Pixel](http://lintcode.com/en/problem/flipped-the-pixel/)| [Python](./Python/flipped-the-pixel.py)| _O(m*n)_ | _O(1)_ | Easy | Google Ladder 18/6 | |
|1555|[Flower Problem](http://lintcode.com/en/problem/flower-problem/)| [Python](./Python/1555-flower-problem.py)| _O(n)_ | _O(n)_ | Hard | Google Ladder 18/6 | Union Find |
|1628|[Driving Problem](http://lintcode.com/en/problem/driving-problem/)| [Python](./Python/1628-driving-problem.py)| _O(n*n)_ | _O(n)_ | Hard | Google Ladder 18/8 | 2D Union Find |
|1631|[Interesting Subarray](http://lintcode.com/en/problem/interesting-subarray/)| [Python](./Python/1631-interesting-subarray.py)| _O(n)_ | _O(n)_ | Medium | Google Ladder 18/8 | Two Pointers |
|1641|[Max Remove Order](http://lintcode.com/en/problem/max-remove-order)| [Python](./Python/1641-max-remove-order.py)| _O(mn)_ | _O(mn)_ | Hard | Google Ladder 18/9 | Union Find |
|1643|[Pick Fruits](http://lintcode.com/en/problem/pick-fruits)| [Python](./Python/1643-pick-fruits.py)| _O(n)_ | _O(n)_ | Medium | Google Ladder 18/9 | Two Pointers |
|1644|[Plane Maximum Rectangle](http://lintcode.com/en/problem/plane-maximum-rectangle)| [Python](./Python/1644-plane-maximum-rectangle.py)| _O(n^2)_ | _O(n)_ | Medium | Google Ladder 18/9 | |



## String
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|13|[strStr](http://lintcode.com/en/problem/strstr/)|[C++](./C++/strstr.cpp)| _O(n + k)_ | _O(k)_ | Easy | LeetCode | `KMP Algorithm` |
|53|[Reverse Words in a String](http://lintcode.com/en/problem/reverse-words-in-a-string/)|[C++](./C++/reverse-words-in-a-string.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode, EPI | |
|54|[String to Integer(atoi)](http://lintcode.com/en/problem/string-to-integeratoi/)|[C++](./C++/string-to-integeratoi.cpp)| _O(n)_ | _O(1)_ | Hard | LeetCode | |
|55|[Compare Strings](http://lintcode.com/en/problem/compare-strings/)|[C++](./C++/compare-strings.cpp)| _O(n)_ | _O(c)_ | Easy | | |
|78|[Longest Common Prefix](http://lintcode.com/en/problem/longest-common-prefix/)|[C++](./C++/longest-common-prefix.cpp)| _O(n)_ | _O(1)_ | Medium | | |
|157|[Unique Characters](http://lintcode.com/en/problem/unique-characters/)|[C++](./C++/unique-characters.cpp)| _O(n)_ | _O(1)_ | Easy | CTCI | |
|158|[Two Strings Are Anagrams](http://lintcode.com/en/problem/two-strings-are-anagrams/)|[C++](./C++/two-strings-are-anagrams.cpp)| _O(n)_ | _O(1)_ | Easy | | |
|171|[Anagrams](http://lintcode.com/en/problem/anagrams/)|[C++](./C++/anagrams.cpp)| _O(n * klogk)_ | _O(m)_ | Easy | LeetCode, EPI | |
|212|[Space Replacement](http://lintcode.com/en/problem/space-replacement/)|[C++](./C++/space-replacement.cpp)| _O(n)_ | _O(1)_ | Easy | | |
|407|[Plus One](http://lintcode.com/en/problem/plus-one.cpp/)|[C++](./C++/plus-one.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|408|[Add Binary](http://lintcode.com/en/problem/add-binary/)|[C++](./C++/add-binary.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|415|[Valid Palindrome](http://lintcode.com/en/problem/valid-palindrome/)|[C++](./C++/valid-palindrome.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|417|[Valid Number](http://lintcode.com/en/problem/valid-number/)|[C++](./C++/valid-number.cpp)| _O(n)_ | _O(1)_ | Hard | LeetCode | Automata |
|420|[Count and Say](http://lintcode.com/en/problem/count-and-say/)|[C++](./C++/count-and-say.cpp)| _O(n * 2^n)_ | _O(2^n)_ | Easy | LeetCode | |
|422|[Length of Last Word](http://lintcode.com/en/problem/length-of-last-word/)|[C++](./C++/length-of-last-word.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|524|[Left Pad](http://lintcode.com/en/problem/left-pad/)|[C++](./C++/left-pad.cpp)| _O(p + n)_ | _O(1)_ | Easy | LeetCode | |
|633|[Find the Duplicate Number](http://lintcode.com/en/problem/find-the-duplicate-number/)|[Python](./Python/633-find-the-duplicate-number.py)| _O(n)_ | _O(1)_ | Hard | Google Ladder 18/7 | fast-slow-pointers |
|1086|[Repeated String Match](http://lintcode.com/en/problem/repeated-string-match/)|[Python](./Python/1086-repeated-string-match.py)| _O(n*(m+n))_ | _O(m+n)_ | Easy | Google Ladder 18/6, LeetCode | |
|1540|[Can Convert](http://lintcode.com/en/problem/can-convert/)|[Python](./Python/1540-can-convert.py)| _O(min(s, t))_ | _O(1)_ | Easy | Google Ladder 18/6 | Two Pointers |
|1542|[Nexttime Norepeat](http://lintcode.com/en/problem/nexttime-norepeat/)|[Python](./Python/1542-nexttime-norepeat.py)| _O(1))_ | _O(1)_ | Easy | Google Ladder 18/6 | |
|1545|[Last Closest Time](http://lintcode.com/en/problem/last-closest-time/)|[Python](./Python/1545-last-closest-time.py)| _O(1))_ | _O(1)_ | Easy | Google Ladder 18/6 | |
|1554|[Lasttime Norepeat](http://lintcode.com/en/problem/lasttime-norepeat/)|[Python](./Python/1554-lasttime-norepeat.py)| _O(1))_ | _O(1)_ | Easy | Google Ladder 18/6 | |
|1580|[Transition String](http://lintcode.com/en/problem/transition-string/)|[Python](./Python/1580-transition-string.py)| _O(n))_ | _O(n)_ | Medium | Google Ladder 18/7 | |
|1625|[Words Compression](http://lintcode.com/en/problem/words-compression/)|[Python](./Python/1625-words-compression.py)| _O(n+k))_ | _O(k)_ | Hard | Google Ladder 18/8 | KMP Algorithm |
|1627|[Word Segmentation](http://lintcode.com/en/problem/word-segmentation/)|[Python](./Python/1627-word-segmentation.py)| _O(n))_ | _O(1)_ | Easy | Google Ladder 18/8 | |
|1632|[Count Email Groups](http://lintcode.com/en/problem/count-email-groups/)|[Python](./Python/1632-count-email-groups.py)| _O(n))_ | _O(n)_ | Easy | Google Ladder 18/8 | |
|1634|[Secret Word](http://lintcode.com/en/problem/secret-word)|[Python](./Python/1634-secret-word.py)| _O((n-w)*w))_ | _O(w)_ | Easy | Google Ladder 18/9 | |
|1642|[Query String](http://lintcode.com/en/problem/query-string)|[Python](./Python/1642-query-string.py)| _O(n))_ | _O(1)_ | Hard | Google Ladder 18/9 | Suffix Tree? |


## Linked List
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|16|[Merge Two Sorted Lists](http://lintcode.com/en/problem/merge-two-sorted-lists/)|[C++](./C++/merge-two-sorted-lists.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode, EPI | |
|35|[Reverse Linked List](http://lintcode.com/en/problem/reverse-linked-list/)|[C++](./C++/reverse-linked-list.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode, EPI | |
|36|[Reverse Linked List II](http://lintcode.com/en/problem/reverse-linked-list-ii/)|[C++](./C++/reverse-linked-list-ii.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode, EPI | |
|96|[Partition List](http://lintcode.com/en/problem/partition-list/)|[C++](./C++/partition-list.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|98|[Sort List](http://lintcode.com/en/problem/sort-list/)|[C++](./C++/sort-list.cpp)| _O(nlogn)_ | _O(logn)_ | Medium | LeetCode, EPI | |
|99|[Reorder List](http://lintcode.com/en/problem/reorder-list/)|[C++](./C++/reorder-list.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|102|[Linked List Cycle](http://lintcode.com/en/problem/linked-list-cycle/)|[C++](./C++/linked-list-cycle.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|103|[Linked List Cycle II](http://lintcode.com/en/problem/linked-list-cycle-ii/)|[C++](./C++/linked-list-cycle-ii.cpp)| _O(n)_ | _O(1)_ | Hard | LeetCode | |
|104|[Merge k Sorted Lists](http://lintcode.com/en/problem/merge-k-sorted-lists/)| [C++](./C++/merge-k-sorted-lists.cpp)| _O(n * logk)_ | _O(1)_ | Medium | LeetCode | Heap, Divide and Conquer |
|105|[Copy List with Random Pointer](http://lintcode.com/en/problem/copy-list-with-random-pointer/)|[C++](./C++/copy-list-with-random-pointer.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|106|[Convert Sorted List to Binary Search Tree](http://lintcode.com/en/problem/convert-sorted-list-to-binary-search-tree/)|[C++](./C++/convert-sorted-list-to-binary-search-tree.cpp)| _O(n)_ | _O(logn)_ | Medium | LeetCode, EPI | |
|112|[Remove Duplicates from Sorted List](http://lintcode.com/en/problem/remove-duplicates-from-sorted-list/)|[C++](./C++/remove-duplicates-from-sorted-list.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode, EPI | |
|113|[Remove Duplicates from Sorted List II](http://lintcode.com/en/problem/remove-duplicates-from-sorted-list-ii/)|[C++](./C++/remove-duplicates-from-sorted-list-ii.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode, EPI | |
|166|[Nth to Last Node in List](http://lintcode.com/en/problem/nth-to-last-node-in-list/)|[C++](./C++/nth-to-last-node-in-list.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|167|[Two Lists Sum](http://lintcode.com/en/problem/two-lists-sum/)|[C++](./C++/two-lists-sum.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|170|[Rotate List](http://lintcode.com/en/problem/rotate-list/)|[C++](./C++/rotate-list.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|173|[Insertion Sort List](http://lintcode.com/en/problem/insertion-sort-list/)|[C++](./C++/insertion-sort-list.cpp)| _O(n^2)_ | _O(1)_ | Easy | LeetCode | |
|174|[Remove Nth Node From End of List](http://lintcode.com/en/problem/remove-nth-node-from-end-of-list/)|[C++](./C++/remove-nth-node-from-end-of-list.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|223|[Palindrome Linked List](http://lintcode.com/en/problem/palindrome-linked-list/)|[C++](./C++/palindrome-linked-list.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|372|[Delete Node in the Middle of Singly Linked List](http://lintcode.com/en/problem/delete-node-in-the-middle-of-singly-linked-list/)|[C++](./C++/delete-node-in-the-middle-of-singly-linked-list.cpp)| _O(1)_ | _O(1)_ | Easy | CTCI | |
|380|[Intersection of Two Linked Lists](http://lintcode.com/en/problem/intersection-of-two-linked-lists/)|[C++](./C++/intersection-of-two-linked-lists.cpp)| _O(m + n)_ | _O(1)_ | Easy | LeetCode | |
|450|[Reverse Nodes in k-Group](http://lintcode.com/en/problem/reverse-nodes-in-k-group/)|[C++](./C++/reverse-nodes-in-k-group.cpp)| _O(n)_ | _O(1)_ | Hard | LeetCode | |
|451|[Swap Nodes in Pairs](http://lintcode.com/en/problem/swap-nodes-in-pairs/)|[C++](./C++/swap-nodes-in-pairs.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|452|[Remove Linked List Elements](http://lintcode.com/en/problem/remove-linked-list-elements/)|[C++](./C++/remove-linked-list-elements.cpp)| _O(n)_ | _O(1)_ | Naive | LeetCode | |
|511|[Swap Two Nodes in Linked List](http://lintcode.com/en/problem/swap-two-nodes-in-linked-list/)|[C++](./C++/swap-two-nodes-in-linked-list.cpp)| _O(n)_ | _O(1)_ | Medium | | |

## Tree
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|7|[Binary Tree Serialization](http://lintcode.com/en/problem/binary-tree-serialization/)| [C++](./C++/binary-tree-serialization.cpp)| _O(n)_ | _O(h)_ | Medium | | |
|85|[Insert Node in a Binary Search Tree](http://lintcode.com/en/problem/insert-node-in-a-binary-search-tree/)| [C++](./C++/insert-node-in-a-binary-search-tree.cpp)| _O(h)_ | _O(1)_ | Easy | | |
|88|[Lowest Common Ancestor](http://lintcode.com/en/problem/lowest-common-ancestor/)| [C++](./C++/lowest-common-ancestor.cpp)| _O(n)_ | _O(h)_ | Medium | EPI | |
|175|[Invert Binary Tree](http://lintcode.com/en/problem/invert-binary-tree/)| [C++](./C++/invert-binary-tree.cpp)| _O(n)_ | _O(h)_ | Easy | LeetCode | |
|442|[Implement Trie](http://lintcode.com/en/problem/implement-trie/)| [C++](./C++/implement-trie.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | Trie |
|1577|[Sum of Leaf Nodes](http://lintcode.com/en/problem/sum-of-leaf-nodes/)| [Python](./Python/sum-of-leaf-nodes.py)| _O(n)_ | _O(1)_ | Hard | Google Ladder 18/7 | Morris |
|1624|[Max Distance](http://lintcode.com/en/problem/max-distance)| [Python](./Python/1624-max-distance.py)| _O(n*l)_ | _O(n*l)_ | Hard | Google Ladder 18/8 | Trie |


## Stack
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|12|[Min Stack](http://lintcode.com/en/problem/min-stack/)| [C++](./C++/min-stack.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode, EPI | |
|40|[Implement Queue by Two Stacks](http://lintcode.com/en/problem/implement-queue-by-two-stacks/)| [C++](./C++/implement-queue-by-two-stacks.cpp)| _O(1), amortized_ | _O(n)_ | Medium | EPI | |
|66|[Binary Tree Preorder Traversal](http://lintcode.com/en/problem/binary-tree-preorder-traversal/)| [C++](./C++/binary-tree-preorder-traversal.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode, EPI | `Morris Traversal` |
|67|[Binary Tree Inorder Traversal](http://lintcode.com/en/problem/binary-tree-inorder-traversal/)| [C++](./C++/binary-tree-inorder-traversal.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode, EPI | `Morris Traversal` |
|68|[Binary Tree Postorder Traversal](http://lintcode.com/en/problem/binary-tree-postorder-traversal/)| [C++](./C++/binary-tree-postorder-traversal.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode, EPI | `Morris Traversal` |
|122|[Largest Rectangle in Histogram](http://lintcode.com/en/problem/largest-rectangle-in-histogram/)| [C++](./C++/largest-rectangle-in-histogram.cpp)| _O(n)_ | _O(n)_ | Hard | LeetCode, EPI | Ascending Stack |
|126|[Max Tree](http://lintcode.com/en/problem/max-tree/)| [C++](./C++/max-tree.cpp)| _O(n)_ | _O(n)_ | Hard | | Descending Stack |
|367|[Expression Tree Build](http://lintcode.com/en/problem/expression-tree-build/)| [C++](./C++/expression-tree-build.cpp)| _O(n)_ | _O(n)_ | Hard | | |
|368|[Expression Evaluation](http://lintcode.com/en/problem/expression-evaluation/)| [C++](./C++/expression-evaluation.cpp)| _O(n)_ | _O(n)_ | Hard | | |
|369|[Convert Expression to Polish Notation](http://lintcode.com/en/problem/convert-expression-to-reverse-notation/)| [C++](./C++/convert-expression-to-polish-notation.cpp)| _O(n)_ | _O(n)_ | Hard | | |
|370|[Convert Expression to Reverse Polish Notation](http://lintcode.com/en/problem/convert-expression-to-reverse-polish-notation/)| [C++](./C++/convert-expression-to-reverse-polish-notation.cpp)| _O(n)_ | _O(n)_ | Hard | | |
|421|[Simplify Path](http://lintcode.com/en/problem/simplify-path/)| [C++](./C++/simplify-path.cpp)| _O(n)_ | _O(n)_ | Medium | LeetCode | |
|423|[Valid Parentheses](http://lintcode.com/en/problem/valid-parentheses.cpp/)| [C++](./C++/valid-parentheses.cpp.cpp)| _O(n)_ | _O(n)_ | Easy | LeetCode | |
|424|[Evaluate Reverse Polish Notation](http://lintcode.com/en/problem/evaluate-reverse-polish-notation/)| [C++](./C++/evaluate-reverse-polish-notation.cpp)| _O(n)_ | _O(n)_ | Medium | LeetCode | |
|473|[Add and Search Word](http://lintcode.com/en/problem/add-and-search-word/)| [C++](./C++/add-and-search-word.cpp)| _O(min(n, h))_ | _O(min(n, h)_ | Medium | LeetCode | Trie |
|510|[Maximal Rectangle](http://lintcode.com/en/problem/maximal-rectangle/)| [C++](./C++/maximal-rectangle.cpp)| _O(m * n)_ | _O(n)_ | Hard | LeetCode | Ascending Stack |
|528|[Flatten Nested List Iterator](http://lintcode.com/en/problem/flatten-nested-list-iterator/)| [C++](./C++/flatten-nested-list-iterator.cpp)| _O(n)_ | _O(h)_ | Medium | LeetCode | |

## Queue
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|362|[Sliding Window Maximum](http://lintcode.com/en/problem/sliding-window-maximum/)| [C++](./C++/sliding-window-maximum.cpp)| _O(n)_ | _O(k)_ | Hard | EPI | Deque, Tricky |

## Heap
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|4|[Ugly Number II](http://lintcode.com/en/problem/ugly-number-ii/)| [C++](./C++/ugly-number-ii.cpp)| _O(n)_ | _O(1)_ | Medium | CTCI | BST, Heap |
|81|[Data Stream Median](http://lintcode.com/en/problem/data-stream-median/)| [C++](./C++/data-stream-median.cpp)| _O(nlogn)_ | _O(n)_ | Hard | EPI | BST, Heap |
|130|[Heapify](http://lintcode.com/en/problem/heapify/)| [C++](./C++/heapify.cpp)| _O(n)_ | _O(1)_ | Medium | | |
|364|[Trapping Rain Water II](http://lintcode.com/en/problem/trapping-rain-water-ii/)| [C++](./C++/trapping-rain-water-ii.cpp)| _O(m * n * (logm + logn))_ | _O(m * n)_ | Hard | | BFS, Heap, Tricky |
|518|[Super Ugly Number](http://lintcode.com/en/problem/super-ugly-number/)| [C++](./C++/super-ugly-number.cpp)| _O(n * k)_ | _O(n + k)_ | Medium | LeetCode | BST, Heap |
|1571|[Top K GPA](http://lintcode.com/en/problem/top-k-gpa/)| [Python](./Python/top-k-gpa.py)| _O(n * logk)_ | _O(k)_ | Medium | Google Ladder 18/7 | Heap |


## Hash Tables
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|56|[2 Sum](http://lintcode.com/en/problem/2-sum/)| [C++](./C++/2-sum.cpp)| _O(n)_ | _O(n)_ | Medium | LeetCode | |
|124|[Longest Consecutive Sequence](http://lintcode.com/en/problem/longest-consecutive-sequence/)| [C++](./C++/longest-consecutive-sequence.cpp)| _O(n)_ | _O(n)_ | Medium | LeetCode, EPI | |
|128|[Hash Function](http://lintcode.com/en/problem/hash-function/)| [C++](./C++/hash-function.cpp)| _O(n)_ | _O(1)_ | Easy | | |
|129|[Rehashing](http://lintcode.com/en/problem/rehashing/)| [C++](./C++/rehashing.cpp)| _O(n)_ | _O(n)_ | Medium | | |
|138|[Subarray Sum](http://lintcode.com/en/problem/subarray-sum/)| [C++](./C++/subarray-sum.cpp)| _O(n)_ | _O(n)_ | Easy | | |
|186|[Max Points on a Line](http://lintcode.com/en/problem/max-points-on-a-line/)| [C++](./C++/max-points-on-a-line.cpp)| _O(n^2)_ | _O(n)_ | Medium | LeetCode | |
|211|[String Permutation](http://lintcode.com/en/problem/string-permutation/)| [C++](./C++/string-permutation.cpp)| _O(n)_ | _O(1)_ | Easy | | |
|384|[Longest Substring Without Repeating Characters](http://lintcode.com/en/problem/longest-substring-without-repeating-characters/)| [C++](./C++/longest-substring-without-repeating-characters.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode, EPI | |
|386|[Longest Substring with At Most K Distinct Characters](http://lintcode.com/en/problem/longest-substring-with-at-most-k-distinct-characters/)| [C++](./C++/longest-substring-with-at-most-k-distinct-characters.cpp)| _O(n)_ | _O(n)_ | Medium | | |
|432|[Find the Weak Connected Component in the Directed Graph](http://lintcode.com/en/problem/find-the-weak-connected-component-in-the-directed-graph/)| [C++](./C++/find-the-weak-connected-component-in-the-directed-graph.cpp)| _O(nlogn)_ | _O(n)_ | Medium | | Union Find |
|434|[Number of Islands II](http://lintcode.com/en/problem/number-of-islands-ii/)| [C++](./C++/number-of-islands-ii.cpp)| _O(k)_ | _O(k)_ | Hard | | Union Find |
|488| [Happy Number](http://lintcode.com/en/problem/happy-number/)      | [C++](./C++/happy-number.cpp)   | _O(k)_  | _O(k)_          | Easy          | LeetCode |
547| [Intersection of Two Arrays](http://lintcode.com/en/problem/intersection-of-two-arrays/) | [C++](./C++/intersection-of-two-arrays.cpp) | _O(m + n)_ | _O(min(m, n))_ | Easy         | EPI, LeetCode | Two Pointers, Binary Search
548| [Intersection of Two Arrays II](http://lintcode.com/en/problem/intersection-of-two-arrays-ii/) | [C++](./C++/intersection-of-two-arrays-ii.cpp) | _O(m + n)_ | _O(min(m, n))_ | Easy         | EPI, LeetCode | Two Pointers, Binary Search
828| [Word Pattern](https://lintcode.com/problem/word-pattern/description) | [Python](./Python/word-pattern.py) | _O(n)_ | _O(n)_ | Easy | |
1443| [longest-ab-substring](https://lintcode.com/problem/longest-ab-substring/description) | [Python](.Python/longest-ab-substring.py) | _O(n)_ | _O(n)_ | Medium | | prefixSum, Hash Table

## Data Structure
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|134|[LRU Cache](http://lintcode.com/en/problem/lru-cache/)| [C++](./C++/lru-cache.cpp)| _O(1)_ | _O(k)_ | Hard | LeetCode, EPI | List, Hash |

## Math
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|2|[Trailing Zeros](http://lintcode.com/en/problem/trailing-zeros/)| [C++](./C++/trailing-zeros.cpp)| _O(1)_ | _O(1)_ | Easy | LeetCode | |
|3|[Digit Counts](http://lintcode.com/en/problem/digit-counts/)| [C++](./C++/digit-counts.cpp)| _O(1)_ | _O(1)_ | Medium | CTCI | |
|114|[Unique Paths](http://lintcode.com/en/problem/unique-paths/)| [C++](./C++/unique-paths.cpp)| _O(min(m, n))_ | _O(1)_ | Easy | LeetCode, CTCI | DP, Math |
|163|[Unique Binary Search Trees](http://lintcode.com/en/problem/unique-binary-search-trees/)| [C++](./C++/unique-binary-search-trees.cpp)| _O(n)_ | _O(1)_ | Medium | CTCI | DP, Math, `Catalan Number` |
|180|[Binary Represention](http://lintcode.com/en/problem/delete-digits/)| [C++](./C++/binary-representation.cpp)| _O(1)_ | _O(1)_ | Hard | CTCI | |
|197|[Permutation Index](http://lintcode.com/en/problem/permutation-index/)| [C++](./C++/permutation-index.cpp)| _O(n^2)_ | _O(1)_ | Easy | | |
|198|[Permutation Index II](http://lintcode.com/en/problem/permutation-index-ii/)| [C++](./C++/permutation-index-ii.cpp)| _O(n^2)_ | _O(n)_ | Medium | | |
|394|[Coins in a Line](http://lintcode.com/en/problem/coins-in-a-line/)| [C++](./C++/coins-in-a-line.cpp)| _O(1)_ | _O(1)_ | Easy | | |
|411|[Gray Code](http://lintcode.com/en/problem/gray-code/)| [C++](./C++/gray-code.cpp)| _O(2^n)_ | _O(1)_ | Medium | LeetCode | |
|413|[Reverse Integer](http://lintcode.com/en/problem/reverse-integer/)| [C++](./C++/reverse-integer.cpp)| _O(1)_ | _O(1)_ | Medium | LeetCode | |
|414|[Divide Two Integer](http://lintcode.com/en/problem/divide-two-integers/)| [C++](./C++/divide-two-integers.cpp)| _O(1)_ | _O(1)_ | Medium | LeetCode | |
|418|[Integer to Roman](http://lintcode.com/en/problem/integer-to-roman/)| [C++](./C++/integer-to-roman.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|419|[Roman to Integer](http://lintcode.com/en/problem/roman-to-integer/)| [C++](./C++/roman-to-integer.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|428| [Pow(x, n)](http://lintcode.com/en/problem/powx-n/)     | [C++](./C++/powx-n.cpp)     | _O(1)_       | _O(1)_       | Medium         | LeetCode ||
|445|[Cosine Similarity](http://lintcode.com/en/problem/cosine-similarity/)| [C++](./C++/cosine-similarity.cpp) [Python](./Python/cosine-similarity.py) | _O(n)_ | _O(1)_ | Easy | | |
|517|[Ugly Number](http://lintcode.com/en/problem/ugly-number/)| [C++](./C++/ugly-number.cpp)| _O(1)_ | _O(1)_ | Easy | CTCI, LeetCode |  |
|1544|[Magic Square](http://lintcode.com/en/problem/magic-square/)| [Python](./Python/magic-square.py)| _O(n*n)_ | _O(n*n)_ | Hard | Google Ladder 18/6 |  |


## Sort
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|5|[Kth Largest Element](http://lintcode.com/en/problem/kth-largest-element/)| [C++](./C++/kth-largest-element.cpp)| _O(n)_ ~ _O(n^2)_ | _O(1)_ | Medium | EPI | Two Pointers, Quick Sort |
|80|[Median](http://lintcode.com/en/problem/median/)| [C++](./C++/median.cpp)| _O(n)_ | _O(1)_ | Easy | EPI | |
|139|[Subarray Sum Closest](http://lintcode.com/en/problem/subarray-sum-closest/)| [C++](./C++/subarray-sum-closest.cpp)| _O(nlogn)_ | _O(n)_ | Medium | | Sort |
|143|[Sort Colors II](http://lintcode.com/en/problem/sort-colors-ii/)| [C++](./C++/sort-colors-ii.cpp)| _O(n)_ | _O(1)_ | Medium | | |
|148|[Sort Colors](http://lintcode.com/en/problem/sort-colors/)| [C++](./C++/sort-colors.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|156|[Merge Intervals](http://lintcode.com/en/problem/merge-intervals/)| [C++](./C++/merge-intervals.cpp)| _O(nlogn)_ | _O(1)_ | Easy | LeetCode, EPI | |
|184|[Largest Number](http://lintcode.com/en/problem/largest-number/)| [C++](./C++/largest-number.cpp)| _O(nlogn)_ | _O(1)_ | Medium | LeetCode | |
|366|[Fibonacci](http://lintcode.com/en/problem/fibonacci/)| [C++](./C++/fibonacci.cpp)| _O(n)_ | _O(1)_ | Easy | | |
|379|[Reorder array to construct the minimum number](http://lintcode.com/en/problem/reorder-array-to-construct-the-minimum-number/)| [C++](./C++/reorder-array-to-construct-the-minimum-number.cpp)| _O(nlogn)_ | _O(1)_ | Medium | LeetCode | |
|387|[The Smallest Difference](http://lintcode.com/en/problem/the-smallest-difference/)| [C++](./C++/the-smallest-difference.cpp)| _O(max(m, n) * log(min(m, n)))_ | _O(1)_ | Medium | | Two Pointers, Binary Search |
|399|[Nuts & Bolts Problem](http://lintcode.com/en/problem/nuts-bolts-problem/)| [C++](./C++/nuts-bolts-problem.cpp)| _O(nlogn)_ | _O(logn)_ | Medium | | Quick Sort |
|400|[Maximum Gap](http://lintcode.com/en/problem/maximum-gap/)| [C++](./C++/maximum-gap.cpp) [Python](./Python/maximum-gap.py)| _O(n)_ | _O(n)_ | Hard | LeetCode | Bucket Sort |
|463|[Sort Integers](http://lintcode.com/en/problem/sort-integers/)| [C++](./C++/sort-integers.cpp)| _O(n^2)_ | _O(1)_ | Easy | | Insertion Sort, Selection Sort, Bubble Sort |
|464|[Sort Integers II](http://lintcode.com/en/problem/sort-integers-ii/)| [C++](./C++/sort-integers-ii.cpp)| _O(nlogn)_ | _O(n)_ | Easy | | Merge Sort, Heap Sort, Quick Sort |
|507|[Wiggle Sort II](http://lintcode.com/en/problem/wiggle-sort-ii/)| [C++](./C++/wiggle-sort-ii.cpp)|  _O(n)_ on average | _O(1)_ | Medium | LeetCode | Tri Partition |
|508|[Wiggle Sort](http://lintcode.com/en/problem/wiggle-sort/)| [C++](./C++/wiggle-sort.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |

## Recursion
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|22|[Flatten List](http://lintcode.com/en/problem/flatten-list/)| [C++](./C++/flatten-list.cpp)| _O(n)_ | _O(h)_ | Easy || |
|72|[Construct Binary Tree from Inorder and Postorder Traversal](http://lintcode.com/en/problem/construct-binary-tree-from-inorder-and-postorder-traversal/)| [C++](./C++/construct-binary-tree-from-inorder-and-postorder-traversal.cpp)| _O(n)_ | _O(n)_ | Medium | LeetCode, EPI | |
|73|[Construct Binary Tree from Preorder and Inorder Traversal](http://lintcode.com/en/problem/construct-binary-tree-from-preorder-and-inorder-traversal/)| [C++](./C++/construct-binary-tree-from-preorder-and-inorder-traversal.cpp)| _O(n)_ | _O(n)_ | Medium | LeetCode, EPI | |
|93|[Balanced Binary Tree](http://lintcode.com/en/problem/balanced-binary-tree/)| [C++](./C++/balanced-binary-tree.cpp) [Python](../../../LeetCode/blob/master/Python/balanced-binary-tree.py) | _O(n)_ | _O(h)_ | Easy | LeetCode | Tree DP |
|94|[Binary Tree Maximum Path Sum](http://lintcode.com/en/problem/binary-tree-maximum-path-sum/)| [C++](./C++/binary-tree-maximum-path-sum.cpp) [Python](../../../LeetCode/blob/master/Python/binary-tree-maximum-path-sum.py) | _O(n)_ | _O(h)_ | Medium | LeetCode | Tree DP |
|95|[Validate Binary Search Tree](http://lintcode.com/en/problem/validate-binary-search-tree/)| [C++](./C++/validate-binary-search-tree.cpp)| _O(n)_ | _O(h)_ | Medium | LeetCode | |
|97|[Maximum Depth of Binary Tree](http://lintcode.com/en/problem/maximum-depth-of-binary-tree/)| [C++](./C++/maximum-depth-of-binary-tree.cpp)| _O(n)_ | _O(h)_ | Easy | LeetCode | |
|131|[Building Outline](http://lintcode.com/en/problem/building-outline/)| [C++](./C++/building-outline.cpp) [Python](./Python/building-outline.py)| _O(nlogn)_ | _O(n)_ | Hard | EPI | Sort, BST |
|140|[Fast Power](http://lintcode.com/en/problem/fast-power/)| [C++](./C++/fast-power.cpp)| _O(logn)_ | _O(1)_ | Medium | | |
|155|[Minimum Depth of Binary Tree](http://lintcode.com/en/problem/minimum-depth-of-binary-tree/)| [C++](./C++/minimum-depth-of-binary-tree.cpp)| _O(n)_ | _O(h)_ | Easy | LeetCode | |
|164|[Unique Binary Search Trees II](http://lintcode.com/en/problem/unique-binary-search-trees-ii/)| [C++](./C++/unique-binary-search-trees-ii.cpp)| _O(n * 4^n / n^(3/2))_ | _O(n)_ | Medium | LeetCode | |
|177|[Convert Sorted Array to Binary Search Tree With Minimal Height](http://lintcode.com/en/problem/convert-sorted-array-to-binary-search-tree-with-minimal-height/)| [C++](./C++/convert-sorted-array-to-binary-search-tree-with-minimal-height.cpp)| _O(n)_ | _O(logn)_ | Easy | LeetCode | |
|201|[Segment Tree Build](http://lintcode.com/en/problem/segment-tree-build/)| [C++](./C++/segment-tree-build.cpp)| _O(n)_ | _O(h)_ | Medium | | Segment Tree, BST |
|202|[Segment Tree Query](http://lintcode.com/en/problem/segment-tree-query/)| [C++](./C++/segment-tree-query.cpp)| _O(h)_ | _O(h)_ | Medium | | Segment Tree, BST |
|203|[Segment Tree Modify](http://lintcode.com/en/problem/segment-tree-modify/)| [C++](./C++/segment-tree-modify.cpp)| _O(h)_ | _O(h)_ | Medium | | Segment Tree, BST |
|205|[Interval Minimum Number](http://lintcode.com/en/problem/interval-minimum-number/)| [C++](./C++/interval-minimum-number.cpp)| build tree: _O(n)_, query: _(h)_ | _O(h)_ | Hard | | Segment Tree, BST |
|206|[Interval Sum](http://lintcode.com/en/problem/interval-sum/)| [C++](./C++/interval-sum.cpp)| build tree: _O(n)_, query: _O(logn)_ | _O(n)_ | Hard | | Segment Tree, BIT |
|207|[Interval Sum II](http://lintcode.com/en/problem/interval-sum-ii/)| [C++](./C++/interval-sum-ii.cpp)| build tree: _O(n)_, query: _O(logn)_, modify: _O(logn)_ | _O(n)_ | Hard | | Segment Tree, BIT |
|245|[Subtree](http://lintcode.com/en/problem/subtree/)| [C++](./C++/subtree.cpp)| _O(m * n)_ | _O(1)_ | Easy | | `Morris Traversal` |
|247|[Segment Tree Query II](http://lintcode.com/en/problem/segment-tree-query-ii/)| [C++](./C++/segment-tree-query-ii.cpp)| _O(h)_ | _O(h)_ | Hard | | Segment Tree, BST |
|248|[Count of Smaller Number](http://lintcode.com/en/problem/count-of-smaller-number/)| [C++](./C++/count-of-smaller-number.cpp)| build tree: _O(n)_, query: _O(logn)_ | _O(h)_ | Medium | | Segment Tree, BST |
|371|[Print Numbers by Recursion](http://lintcode.com/en/problem/print-numbers-by-recursion/)| [C++](./C++/print-numbers-by-recursion.cpp)| _O(n)_ | _O(n)_ | Medium | | |
|375|[Clone Binary Tree](http://lintcode.com/en/problem/clone-binary-tree/)| [C++](./C++/clone-binary-tree.cpp)| _O(n)_ | _O(h)_ | Easy | | |
|378|[Convert Binary Search Tree to Doubly Linked List](http://lintcode.com/en/problem/convert-binary-search-tree-to-doubly-linked-list/)| [C++](./C++/convert-binary-search-tree-to-doubly-linked-list.cpp)| _O(n)_ | _O(h)_ | Medium | | |
|439|[Segment Tree Build II](http://lintcode.com/en/problem/segmemt-tree-build-ii/)| [C++](./C++/segment-tree-build-ii.cpp)| _O(n)_ | _O(h)_ | Medium | | Segment Tree, BST |
|453|[Flatten Binary Tree to Linked List](http://lintcode.com/en/problem/flatten-binary-tree-to-linked-list/)|[C++](./C++/flatten-binary-tree-to-linked-list.cpp)| _O(n)_ | _O(h)_ | Easy | LeetCode | |
|469| [Identical Binary Tree](http://lintcode.com/en/problem/problems/identical-binary-tree/)     | [C++](./C++/identical-binary-tree.cpp)     | _O(n)_       | _O(h)_       | Easy         |||
|532|[Reverse Pairs](http://lintcode.com/en/problem/reverse-pairs/)| [C++](./C++/reverse-pairs.cpp)| _O(nlogn)_ | _O(n)_ | Medium | variant of [Count of Smaller Number before itself](http://lintcode.com/en/problem/count-of-smaller-number-before-itself/) | BIT, Merge Sort |
|535|[House Robber III](http://lintcode.com/en/problem/house-robber-iii/)| [C++](./C++/house-robber-iii.cpp)| _O(n)_ | _O(h)_ | Medium | LeetCode | |
|XXX|[Topological Sort](http://lintcode.com/en/problem/topological-sort/)| [Python](./Python/topological-sort.py)| _O(V+E)_ | _O(h)_ | Medium | | Topological Sort |



## Binary Search
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|14|[First Position of Target](http://lintcode.com/en/problem/first-position-of-target/)| [C++](./C++/first-position-of-target.cpp)| _O(logn)_ | _O(1)_ | Easy | | |
|28|[Search a 2D Matrix](http://lintcode.com/en/problem/search-a-2d-matrix/)| [C++](./C++/search-a-2d-matrix.cpp)| _O(logm + logn)_ | _O(1)_ | Easy | LeetCode | |
|60|[Search Insert Position](http://lintcode.com/en/problem/search-insert-position/)| [C++](./C++/search-insert-position.cpp)| _O(logn)_ | _O(1)_ | Easy | LeetCode | |
|61|[Search for a Range](http://lintcode.com/en/problem/search-for-a-range/)| [C++](./C++/search-for-a-range.cpp)| _O(logn)_ | _O(1)_ | Medium | LeetCode | |
|62|[Search in Rotated Sorted Array](http://lintcode.com/en/problem/search-in-rotated-sorted-array/)| [C++](./C++/search-in-rotated-sorted-array.cpp)| _O(logn)_ | _O(1)_ | Medium | LeetCode | |
|63|[Search in Rotated Sorted Array II](http://lintcode.com/en/problem/search-in-rotated-sorted-array-ii/)| [C++](./C++/search-in-rotated-sorted-array-ii.cpp)| _O(logn)_ | _O(1)_ | Medium | LeetCode | |
|65|[Median of two Sorted Arrays](http://lintcode.com/en/problem/median-of-two-sorted-arrays/)| [C++](./C++/median-of-two-sorted-arrays.cpp)| _O(log(min(m, n)))_ | _O(1)_ | Hard | LeetCode, EPI | Tricky |
|74|[First Bad Version](http://lintcode.com/en/problem/first-bad-version/)| [C++](./C++/first-bad-version.cpp)| _O(logn)_ | _O(1)_ | Medium | | |
|75|[Find Peak Element](http://lintcode.com/en/problem/find-peak-element/)| [C++](./C++/find-peak-element.cpp) [Python](./Python/find-peak-element.py)| _O(logn)_ | _O(1)_ | Medium | LeetCode | |
|76|[Longest Increasing Subsequence](http://lintcode.com/en/problem/longest-increasing-subsequence/)| [C++](./C++/longest-increasing-subsequence.cpp) [Python](./Python/76-longest-increasing-subsequence.py) | _O(nlogn)_ | _O(n)_ | Medium | CTCI, Leetcode | |
|141|[Sqrt(x)](http://lintcode.com/en/problem/sqrtx/)| [C++](./C++/sqrtx.cpp)| _O(logn)_ | _O(1)_ | Easy | LeetCode | |
|159|[Find Minimum in Rotated Sorted Array](http://lintcode.com/en/problem/find-minimum-in-rotated-sorted-array/)| [C++](./C++/find-minimum-in-rotated-sorted-array.cpp)| _O(logn)_ | _O(1)_ | Medium | LeetCode | |
|160|[Find Minimum in Rotated Sorted Array II](http://lintcode.com/en/problem/find-minimum-in-rotated-sorted-array-ii/)| [C++](./C++/find-minimum-in-rotated-sorted-array-ii.cpp)| _O(logn)_ | _O(1)_ | Medium | LeetCode | |
|183|[Wood Cut](http://lintcode.com/en/problem/wood-cut/)| [C++](./C++/wood-cut.cpp)| _O(nlogL)_ | _O(1)_ | Medium | | |
|390|[Find Peak Element II](http://lintcode.com/en/problem/find-peak-element-ii/)| [C++](./C++/find-peak-element-ii.cpp) [Java](./Java/find-peak-element-ii.java) [Python](./Python/find-peak-element-ii.py)| _O(m + n)_ | _O(1)_ | Hard | | |
|437|[Copy Books](http://lintcode.com/en/problem/copy-books/)| [C++](./C++/copy-books.cpp) | _O(nlogp)_ | _O(1)_ | Hard | UVa 714 | |
|458|[Last Position of Target](http://lintcode.com/en/problem/last-position-of-target/)| [Python](./Python/458-last-position-of-target.py) | _O(logn)_ | _O(1)_ | Easy | Google Ladder 18/7 | |
|1564|[Interval Search](http://lintcode.com/en/problem/interval-search/)| [Python](./Python/1564-interval-search.py) | _O(logn)_ | _O(1)_ | Easy | Google Ladder 18/7 | |
|1623|[Minimal Distance in the Array](http://lintcode.com/en/problem/minimal-distance-in-the-array/)| [Python](./Python/1623-minimal-distance-in-the-array.py) | _O(min(MlogN, NlogN))_ | _O(1)_ |  | Google Ladder 18/8 | |
|1626|[Salary Adjustment](http://lintcode.com/en/problem/salary-adjustment/)| [Python](./Python/1626-salary-adjustment.py) | _O(log(target/n))_ | _O(1)_ | Easy | Google Ladder 18/8 | |
|1633|[Strings that Satisfies the Condition](http://lintcode.com/en/problem/strings-that-satisfies-the-condition)| [Python](./Python/1633-strings-that-satisfies-the-condition.py) | _O(n*len(s))_ | _O(1)_ | Easy | Google Ladder 18/9 | |
|1629|[Find the Nearest Store](http://lintcode.com/en/problem/find-the-nearest-store)| [Python](./Python/1629-find-the-nearest-store.py) | _O(min(HlogS, SlogS))_ | _O(1)_ | Easy | Google Ladder 18/8 | |
|1645|[Least Subsequences](http://lintcode.com/en/problem/least-subsequences)| [Python](./Python/1645-least-subsequences.py) | _O(nlogn)_ | _O(n)_ | Medium | Google Ladder 18/9 | |



## Breadth-First Search
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|69|[Binary Tree Level Order Traversal](http://lintcode.com/en/problem/binary-tree-level-order-traversal/)| [C++](./C++/binary-tree-level-order-traversal.cpp)| _O(n)_ | _O(n)_ | Medium | LeetCode | BFS |
|70|[Binary Tree Level Order Traversal II](http://lintcode.com/en/problem/binary-tree-level-order-traversal-ii/)| [C++](./C++/binary-tree-level-order-traversal-ii.cpp)| _O(n)_ | _O(n)_ | Medium | LeetCode | BFS |
|71|[Binary Tree Zigzag Level Order Traversal](http://lintcode.com/en/problem/binary-tree-zigzag-level-order-traversal/)| [C++](./C++/binary-tree-zigzag-level-order-traversal.cpp)| _O(n)_ | _O(n)_ | Medium | LeetCode | BFS |
|120|[Word Ladder](http://lintcode.com/en/problem/word-ladder/)| [C++](./C++/word-ladder.cpp)| _O(n * d)_ | _O(d)_ | Medium | LeetCode | BFS |
|121|[Word Ladder II](http://lintcode.com/en/problem/word-ladder-ii/)| [C++](./C++/word-ladder-ii.cpp)| _O(n * d)_ | _O(d)_ | Hard | LeetCode | BFS, Back Trace |
|127|[Topological Sorting](http://lintcode.com/en/problem/topological-sorting/)| [C++](./C++/topological-sorting.cpp)| _O(\|V\|+\|E\|)_ | _O(\|E\|)_ | Medium | | DFS, BFS |
|137|[Clone Graph](http://lintcode.com/en/problem/clone-graph/)| [C++](./C++/clone-graph.cpp)| _O(\|V\|+\|E\|)_ | _O(\|V\|)_ | Medium | | BFS |
|176|[Route Between Two Nodes in Graph](http://lintcode.com/en/problem/route-between-two-nodes-in-graph/)| [C++](./C++/route-between-two-nodes-in-graph.cpp)| _O(n)_ | _O(n)_ | Medium | | DFS, BFS |
|178| [Graph Valid Tree](http://lintcode.com/en/problem/graph-valid-tree/)| [C++](./C++/graph-valid-tree.cpp) | _O(\|V\| + \|E\|)_          | _O(\|V\| + \|E\|)_          | Medium         | LeetCode ||
|431|[Find the Connected Component in the Undirected Graph](http://lintcode.com/en/problem/find-the-connected-component-in-the-undirected-graph/)| [C++](./C++/find-the-connected-component-in-the-undirected-graph.cpp)| _O(n)_ | _O(n)_ | Medium | | BFS |
|477|[Surrounded Regions](http://lintcode.com/en/problem/surrounded-regions/)|[C++](./C++/surrounded-regions.cpp)| _O(m * n)_ | _O(m + n)_ | Medium         | LeetCode ||
|630|[Knight Shortest Path II](http://lintcode.com/en/problem/knight-shortest-path-ii)|[Python](./Python/knight-shortest-path-ii.py)| _O(m * n)_ | _O(m * n)_ | Easy | | BFS or DP |
|825|[Bus Station](http://lintcode.com/en/problem/bus-station)|[Python](./Python/bus-station.py) | _O(#of stops)_ |  _O(#of stops)_ | Hard | Google Ladder 18/6 | |


## Depth-First Search
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|90|[K Sum II](http://lintcode.com/en/problem/k-sum-ii/)| [C++](./C++/k-sum-ii.cpp)| _O(k * C(n, k))_ | _O(k)_ | Medium | | |
|376|[Binary Tree Path Sum](http://lintcode.com/en/problem/binary-tree-path-sum/)| [C++](./C++/binary-tree-path-sum.cpp)| _O(n)_ | _O(h)_ | Easy | LeetCode | |
|433|[Number of Islands](http://lintcode.com/en/problem/number-of-islands/)| [C++](./C++/number-of-islands.cpp)| _O(m * n)_ | _O(m * n)_ | Easy | LeetCode | DFS |
|480| [Binary Tree Paths](http://lintcode.com/en/problem/binary-tree-paths/) | [C++](./C++/binary-tree-paths.cpp) | _O(n * h)_ | _O(h)_ | Easy         | LeetCode ||
|795|[4-Way Unique Pathsp](http://lintcode.com/en/problem/4-way-unique-paths)| [Python](./Python/4-way-unique-paths.py)| _O(m*n)_ | _O(m*n)_ | Medium | | |
|1630|[Interesting String](http://lintcode.com/en/problem/interesting-string)| [Python](./Python/1630-interesting-string.py)| | _O(n)_ | Medium | Google Ladder 18/8 | |
|1646|[CheckWords](http://lintcode.com/en/problem/checkwords)| [Python](./Python/1646-checkwords.py)| | _O(n)_ | Easy | Google Ladder 18/9 | DFS + Memorization |



## Backtracking
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|15|[Permutations](http://lintcode.com/en/problem/permutations/)| [C++](./C++/permutations.cpp)| _O(n * n!)_ | _O(n)_ | Medium | LeetCode, EPI | |
|16|[Permutations II](http://lintcode.com/en/problem/permutations-ii/)| [C++](./C++/permutations-ii.cpp)| _O(n * n!)_ | _O(n)_ | Medium | LeetCode, EPI | |
|17|[Subsets](http://lintcode.com/en/problem/subsets/)| [C++](./C++/subsets.cpp)| _O(n * 2^n)_ | _O(1)_ | Medium | LeetCode | |
|18|[Subsets II](http://lintcode.com/en/problem/subsets-ii/)| [C++](./C++/subsets-ii.cpp)| _O(n * 2^n)_ | _O(1)_ | Medium | LeetCode | |
|33|[N-Queens](http://lintcode.com/en/problem/n-queens/)| [C++](./C++/n-queens.cpp)| _O(n * n!)_ | _O(n)_ | Medium | LeetCode, EPI | |
|34|[N-Queens II](http://lintcode.com/en/problem/n-queens-ii/)| [C++](./C++/n-queens-ii.cpp)| _O(n * n!)_ | _O(n)_ | Medium | LeetCode, EPI | |
|123|[Word Search](http://lintcode.com/en/problem/word-search/)| [C++](./C++/word-search.cpp)| _O(m * n * l)_ | _O(l)_ | Medium | LeetCode | |
|132|[Word Search II](http://lintcode.com/en/problem/word-search-ii/)| [C++](./C++/word-search-ii.cpp)| _O(m * n * l)_ | _O(l)_ | Hard | | Trie, DFS |
|135|[Combination Sum](http://lintcode.com/en/problem/combination-sum/)| [C++](./C++/combination-sum.cpp)| _O(k * n^k)_ | _O(k)_ | Medium | LeetCode | DFS |
|136|[Palindrome Partitioning](http://lintcode.com/en/problem/palindrome-partitioning/)| [C++](./C++/palindrome-partitioning.cpp)| _O(2^n)_ | _O(n)_ | Easy | LeetCode, EPI | |
|152|[Combinations](http://lintcode.com/en/problem/combinations/)| [C++](./C++/combinations.cpp)| _O(k * n^k)_ | _O(k)_ | Medium | LeetCode, EPI | |
|153|[Combination Sum II](http://lintcode.com/en/problem/combination-sum-ii/)| [C++](./C++/combination-sum-ii.cpp)| _O(k * C(n, k))_ | _O(k)_ | Medium | LeetCode | DFS |
|425|[Letter Combinations of a Phone Number](http://lintcode.com/en/problem/letter-combinations-of-a-phone-number/) | [C++](./C++/letter-combinations-of-a-phone-number.cpp)| _O(n * 4^n)_ | _O(n)_ | Medium | LeetCode | |
|426| [Restore IP Addresses](http://lintcode.com/en/problem/restore-ip-addresses/) | [C++](./C++/restore-ip-addresses.cpp) | _O(1)_ | _O(1)_ | Medium         | LeetCode ||[C++](./C++/letter-combinations-of-a-phone-number.cpp)| _O(n * 4^n)_ | _O(n)_ | Medium | LeetCode | |
|427| [Generate Parentheses](http://lintcode.com/en/problem/generate-parentheses/)| [C++](./C++/generate-parentheses.cpp)| _O(4^n / n^(3/2))_ | _O(n)_   | Medium         | LeetCode ||
|1576| [Optimal Match](http://lintcode.com/en/problem/optimal-match)| [Python](./Python/optimal-match.py)| ?? | _O(n)_   | Hard | Google Ladder 18/9 | Hungary Algorithm |


## Binary Search Trees
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|11|[Search Range in Binary Search Tree](http://lintcode.com/en/problem/search-range-in-binary-search-tree/)| [C++](./C++/search-range-in-binary-search-tree.cpp)| _O(n)_ | _O(h)_ | Medium | EPI | |
|86|[Binary Search Tree Iterator](http://lintcode.com/en/problem/binary-search-tree-iterator/)| [C++](./C++/binary-search-tree-iterator.cpp)| _O(1)_ | _O(h)_ | Hard | LeetCode | |
|87|[Remove Node in Binary Search Tree](http://lintcode.com/en/problem/remove-node-in-binary-search-tree/)| [C++](./C++/remove-node-in-binary-search-tree.cpp)| _O(h)_ | _O(h)_ | Hard | | |
|249|[Count of Smaller Number before itself](http://lintcode.com/en/problem/count-of-smaller-number-before-itself/)| [C++](./C++/count-of-smaller-number-before-itself.cpp)| _O(nlogn)_ | _O(n)_ | Hard | | BST, BIT, Divide and Conquer, Merge Sort |
|360|[Sliding Window Median](http://lintcode.com/en/problem/sliding-window-median/)| [C++](./C++/sliding-window-median.cpp)| _O(nlogw)_ | _O(w)_ | Hard | | BST, Tricky |
|391|[Number of Airplanes in the Sky](http://lintcode.com/en/problem/number-of-airplanes-in-the-sky/)| [C++](./C++/number-of-airplanes-in-the-sky.cpp)| _O(nlogn)_ | _O(n)_ | Easy | | BST, Heap |
|401|[Kth Smallest Number in Sorted Matrix](http://lintcode.com/en/problem/kth-smallest-number-in-sorted-matrix/)| [C++](./C++/kth-smallest-number-in-sorted-matrix.cpp)| _O(klog(min(m, n, k)))_ | _O(min(m, n, k))_ | Medium | | BST, Heap |
|902|[Kth Smallest Element in a BST](http://lintcode.com/en/problem/kth-smallest-element-in-a-bst/)| [Python](./Python/902-kth-smallest-element-in-a-bst.py)| _O(k)_ | _O(k)_ | Easy | Google Ladder 18/7 | BST |

## Dynamic Programming
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|20|[Dices Sum](http://lintcode.com/en/problem/dices-sum/)| [C++](./C++/dices-sum.cpp)| _O(n^2)_ | _O(n)_ | Hard | | |
|29|[Interleaving String](http://lintcode.com/en/problem/interleaving-string/)| [C++](./C++/interleaving-string.cpp)| _O(m * n)_ | _O(min(m, n))_ | Medium | EPI | |
|43|[Maximum Subarray III](http://lintcode.com/en/problem/maximum-subarray-iii/)| [C++](./C++/maximum-subarray-iii.cpp)| _O(k * n)_ | _O(k * n)_ | Hard | | |
|77|[Longest Common Subsequence](http://lintcode.com/en/problem/longest-common-subsequence/)| [C++](./C++/longest-common-subsequence.cpp)| _O(m * n)_ | _O(min(m, n))_ | Medium | | |
|79|[Longest Common Substring](http://lintcode.com/en/problem/longest-common-substring/)| [C++](./C++/longest-common-substring.cpp)| _O(m * n)_ | _O(min(m, n))_ | Medium | | |
|89|[K Sum](http://lintcode.com/en/problem/k-sum/)| [C++](./C++/k-sum.cpp)| _O(k * n * t)_ | _O(n * t)_ | Hard | | |
|91|[Minimum Adjustment Cost](http://lintcode.com/en/problem/minimum-adjustment-cost/)| [C++](./C++/minimum-adjustment-cost.cpp)| _O(k * n * t)_ | _O(k)_ | Medium | | |
|92|[Backpack](http://lintcode.com/en/problem/backpack/)| [C++](./C++/backpack.cpp) [Python](./Python/backpack.py) | _O(m * n)_ | _O(m)_ | Easy | | |
|107|[Word Break](http://lintcode.com/en/problem/word-break/)| [C++](./C++/word-break.cpp)| _O(n * l^2)_ | _O(n)_ | Medium | LeetCode, EPI | |
|108|[Palindrome Partitioning II](http://lintcode.com/en/problem/palindrome-partitioning-ii/)| [C++](./C++/palindrome-partitioning-ii.cpp)| _O(n^2)_ | _O(n)_ | Medium | LeetCode, EPI | |
|109|[Triangle](http://lintcode.com/en/problem/triangle/)| [C++](./C++/triangle.cpp) [Python](./Python/109-triangle.py) | _O(n)_ | _O(n)_ | Easy | LeetCode, EPI | |
|110|[Minimum Path Sum](http://lintcode.com/en/problem/minimum-path-sum/)| [C++](./C++/minimum-path-sum.cpp)| _O(m * n)_ | _O(min(m, n))_ | Easy | LeetCode, EPI | |
|111|[Climbing Stairs](http://lintcode.com/en/problem/climbing-stairs/)| [C++](./C++/climbing-stairs.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|115|[Unique Paths II](http://lintcode.com/en/problem/unique-paths-ii/)| [C++](./C++/unique-paths-ii.cpp)| _O(m * n)_ | _O(min(m, n))_ | Easy | LeetCode, CTCI | DP, Math |
|118|[Distinct Subsequences](http://lintcode.com/en/problem/distinct-subsequences/)| [C++](./C++/distinct-subsequences.cpp)| _O(m * n)_ | _O(m)_ | Medium | LeetCode | DP |
|119|[Edit Distance](http://lintcode.com/en/problem/edit-distance/)| [C++](./C++/edit-distance.cpp)| _O(m * n)_ | _O(min(m, n))_ | Medium | LeetCode, CTCI | DP |
|125|[Backpack II](http://lintcode.com/en/problem/backpack-ii/)| [C++](./C++/backpack-ii.cpp)| _O(m * n)_ | _O(m)_ | Medium | | |
|149|[Best Time to Buy and Sell Stock](http://lintcode.com/en/problem/best-time-to-buy-and-sell-stock/)| [C++](./C++/best-time-to-buy-and-sell-stock.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode, EPI | |
|150|[Best Time to Buy and Sell Stock II](http://lintcode.com/en/problem/best-time-to-buy-and-sell-stock-ii/)| [C++](./C++/best-time-to-buy-and-sell-stock-ii.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode, EPI | |
|151|[Best Time to Buy and Sell Stock III](http://lintcode.com/en/problem/best-time-to-buy-and-sell-stock-iii/)| [C++](./C++/best-time-to-buy-and-sell-stock-iii.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode, EPI | |
|154|[Regular Expression Matching](http://lintcode.com/en/problem/regular-expression-matching/)| [C++](./C++/regular-expression-matching.cpp)| _O(m * n)_ | _O(m)_ | Hard | LeetCode | DP, Recursion |
|168|[Burst Balloons](http://lintcode.com/en/problem/burst-balloons/)| [C++](./C++/burst-balloons.cpp)| _O(n^3)_ | _O(n^2)_ | Medium | LeetCode | |
|191|[Maximum Product Subarray](http://lintcode.com/en/problem/maximum-product-subarray/)| [C++](./C++/maximum-product-subarray.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|392|[House Robber](http://lintcode.com/en/problem/house-robber/)| [C++](./C++/house-robber.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|393|[Best Time to Buy and Sell Stock IV](http://lintcode.com/en/problem/best-time-to-buy-and-sell-stock-iv/)| [C++](./C++/best-time-to-buy-and-sell-stock-iv.cpp)| _O(k * n)_ | _O(k)_ | Hard | LeetCode, EPI | |
|395|[Coins in a Line II](http://lintcode.com/en/problem/coins-in-a-line-ii/)| [C++](./C++/coins-in-a-line-ii.cpp)| _O(n)_ | _O(1)_ | Medium | | |
|396|[Coins in a Line III](http://lintcode.com/en/problem/coins-in-a-line-iii/)| [C++](./C++/coins-in-a-line-iii.cpp)| _O(n^2)_ | _O(n)_ | Hard | | |
|397|[Longest Increasing Continuous subsequence](http://lintcode.com/en/problem/longest-increasing-continuous-subsequence/)| [C++](./C++/longest-increasing-continuous-subsequence.cpp)| _O(n)_ | _O(1)_ | Easy | | |
|398|[Longest Increasing Continuous subsequence II](http://lintcode.com/en/problem/longest-increasing-continuous-subsequence-ii/)| [C++](./C++/longest-increasing-continuous-subsequence-ii.cpp)| _O(m * n)_ | _O(m * n)_ | Hard | | |
|403|[Continuous Subarray Sum II](http://lintcode.com/en/problem/continuous-subarray-sum-ii/)| [C++](./C++/continuous-subarray-sum-ii.cpp)| _O(n)_ | _O(1)_ | Medium | EPI | |
|430|[Scramble String](http://lintcode.com/en/problem/scramble-string/)| [C++](./C++/scramble-string.cpp)| _O(n^4)_ | _O(n^3)_ | Hard | LeetCode | |
|435|[Post Office Problem](http://lintcode.com/en/problem/post-office-problem/)| [C++](./C++/post-office-problem.cpp)| _O(k * n^2)_ | _O(n)_ | Hard | PKU 1160 | |
|436|[Maximal Square](http://lintcode.com/en/problem/maximal-square/)| [C++](./C++/maximal-square.cpp)| _O(m * n)_ | _O(n)_ | Medium | LeetCode | |
|512|[Decode Ways](http://lintcode.com/en/problem/decode-ways/)| [C++](./C++/decode-ways.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|513|[Perfect Squares](http://lintcode.com/en/problem/perfect-squares/)| [C++](./C++/perfect-squares.cpp)| _O(n * sqrt(n))_ | _O(n)_ | Medium | LeetCode | |
|514|[Paint Fence](http://lintcode.com/en/problem/paint-fence/)| [C++](./C++/paint-fence.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|515|[Paint House](http://lintcode.com/en/problem/paint-house/)| [C++](./C++/paint-house.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|516|[Paint House II](http://lintcode.com/en/problem/paint-house-ii/)| [C++](./C++/paint-house-ii.cpp)| _O(n * k)_ | _O(k)_ | Hard | LeetCode | |
|534|[House Robber II](http://lintcode.com/en/problem/house-robber-ii/)| [C++](./C++/house-robber-ii.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|564|[Backpack VI](http://lintcode.com/en/problem/backpack-vi/)| [C++](./C++/backpack-vi.cpp)| _O(n * t)_ | _O(t)_ | Medium | | |
|630|[Knight Shortest Path II](http://lintcode.com/en/problem/knight-shortest-path-ii/)| [Python](./Python/knight-shortest-path-ii.py)| _O(m * n)_ | _O(m * n)_ | Easy | | |
|631|[Maximal Square II](http://lintcode.com/en/problem/maximal-square-ii/)| [Python](./Python/maximal-square-ii.py)| _O(m * n)_ | _O(n)_ | Easy | | Amazon |
|741|[Calculate Maximum Value II](http://lintcode.com/en/problem/calculate-maximum-value-ii)| [Python](./Python/calculate-maximum-value-ii.py)| _O(n^2)_ | _O(n^2)_ | Easy | | Interval DP |
|843|[Digital Flip](http://lintcode.com/en/problem/digital-flip)| [Python](./Python/digital-flip.py)| _O(n)_ | _O(1)_ | Medium | Microsoft | |
|953|[The Biggest Score On The Tree](http://lintcode.com/en/problem/the-biggest-score-on-the-tree)| [Python](./Python/the-biggest-score-on-the-tree.py)| _O(n)_ | _O(h)_ | Medium | Airbnb | Tree DP |
|1224|[Count The Repetitions](http://lintcode.com/en/problem/count-the-repetitions)| [Python](./Python/count-the-repetitions.py)| _O(n1 * len(s1))_ | _O(n1)_ | Super Hard | | |
|1383|[Subtree Count](http://lintcode.com/en/problem/subtree-count)| [Python](./Python/subtree-count.py)| _O(n)_ | _O(n)_ | Medium | | |
|1384|[Segment Stones Merge](http://lintcode.com/en/problem/segment-stones-merge)| [Python](./Python/segment-stones-merge.py) [C++](./C++/segment-stones-merge.cpp) [Java](./Java/segment-stones-merge.java)| _O(n^3)_ | _O(n^3)_ | Super Hard | | 3d DP |
|1395|[The Barycentre Of The Trees](http://lintcode.com/en/problem/the-barycentre-of-the-trees)| [Python](./Python/the-barycentre-of-the-trees.py)| _O(n)_ | _O(n)_ | Hard | Facebook | Tree DP |
|1400|[Fermat Point Of Graphs](http://lintcode.com/en/problem/fermat-point-of-graphs)| [Python](./Python/fermat-point-of-graphs.py)| _O(n)_ | _O(n)_ | Super Hard | Google | Tree DP |
|1414|[Eat The Beans](http://lintcode.com/en/problem/eat-the-beans)| [Python](./Python/eat-the-beans.py) [C++](./C++/eat-the-beans.cpp)| _O(w*r)_ | _O(w*r)_ | Medium | Twitter | |
|1444|[Dyeing Problem](http://lintcode.com/en/problem/dyeing-problem)| [Python](./Python/dyeing-problem.py)| _O(n)_ | _O(1)_ | Medium | Alibaba | |
|1447|[Calculation the Sum of Path](http://lintcode.com/en/problem/calculation-the-sum-of-path)| [Python](./Python/calculation-the-sum-of-path.py) [C++](./C++/calculation-the-sum-of-path.cpp) [Java](./Java/calculation-the-sum-of-path.java)| _O(l * w)_ | _O(l * w)_ | Medium | Google | |
|1448|[Card Game](http://lintcode.com/en/problem/card-game)| [Python](./Python/card-game.py) [C++](./C++/card-game.cpp) [Java](./Java/card-game.java)| _O(n * totalProfit * totalCost)_ | _O(totalProfit * totalCost)_ | Medium | Google | |
|1470|[The Game Of Take Numbers](http://lintcode.com/en/problem/the-game-of-take-numbers)| [Python](./Python/1470-the-game-of-take-numbers.py) | _O(n*n)_ | _O(n)_ | Medium | Google Ladder 18/7 | Interval |
|1538|[Card Game II](http://lintcode.com/en/problem/card-game-ii)| [Python](./Python/1538-card-game-ii.py) | _O(n * totalMoney)_ | _O(totalMoney)_ | Easy | Google Ladder 18/6 | backpack |
|1541|[Put Box](http://lintcode.com/en/problem/put-box)| [Python](./Python/1541-put-box.py) | _O(m*n)_ | _O(m*n)_ | Medium | Google Ladder 18/6 | Interval |
|1543|[Unique Path IV](http://lintcode.com/en/problem/unique-path-iv)| [Python](./Python/1543-unique-path-iv.py) | _O(h*w)_ | _O(h)_ | Medium | Google Ladder 18/6| Coordinate |
|1621|[Cut Connection](http://lintcode.com/en/problem/cut-connection/)| [Python](./Python/1621-cut-connection.py)| _O(m*n)_ | _O(1)_ | Medium | Google Ladder 18/8 | Coordinate |
|1640|[Duplicate Digits](http://lintcode.com/en/problem/duplicate-digits)| [Python](./Python/1640-duplicate-digits.py)| | _O(1)_ | Hard | Google Ladder 18/9 | |



## Greedy
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|41|[Maximum Subarray](http://lintcode.com/en/problem/maximum-subarray/)| [C++](./C++/maximum-subarray.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|42|[Maximum Subarray II](http://lintcode.com/en/problem/maximum-subarray-ii/)| [C++](./C++/maximum-subarray-ii.cpp)| _O(n)_ | _O(n)_ | Medium | | |
|44|[Minimum Subarray](http://lintcode.com/en/problem/minimum-subarray/)| [C++](./C++/minimum-subarray.cpp)| _O(n)_ | _O(1)_ | Easy | | |
|45|[Maximum Subarray Difference](http://lintcode.com/en/problem/maximum-subarray-difference/)| [C++](./C++/maximum-subarray-difference.cpp)| _O(n)_ | _O(n)_ | Medium | | |
|116|[Jump Game](http://lintcode.com/en/problem/jump-game/)| [C++](./C++/jump-game.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|117|[Jump Game II](http://lintcode.com/en/problem/jump-game-ii/)| [C++](./C++/jump-game-ii.cpp)| _O(n)_ | _O(1)_ | Medium | LeetCode | |
|182|[Delete Digits](http://lintcode.com/en/problem/delete-digits/)| [C++](./C++/delete-digits.cpp)| _O(n)_ | _O(n)_ | Medium | | |
|187|[Gas Station](http://lintcode.com/en/problem/gas-station/)| [C++](./C++/gas-station.cpp)| _O(n)_ | _O(1)_ | Easy | LeetCode | |
|192|[Wildcard Matching](http://lintcode.com/en/problem/wildcard-matching/)| [C++](./C++/wildcard-matching.cpp)| _O(m + n)_ | _O(1)_ | Hard | LeetCode | Greedy, DP, Recursion |
|402|[Continuous Subarray Sum](http://lintcode.com/en/problem/continuous-subarray-sum/)| [C++](./C++/continuous-subarray-sum.cpp)| _O(n)_ | _O(1)_ | Medium | EPI | |
|412|[Candy](http://lintcode.com/en/problem/candy/)| [C++](./C++/candy.cpp)| _O(n)_ | _O(n)_ | Hard | LeetCode | Greedy |
|552| [Create Maximum Number](http://lintcode.com/en/problem/create-maximum-number/)| [C++](./C++/create-maximum-number.cpp) | _O(k * (m + n + k))_ ~ _O(k * (m + n + k^2))_| _O(m + n + k^2)_ | Hard | LeetCode | Greedy, DP|

## OO Design
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|204|[Singleton](http://lintcode.com/en/problem/singleton/)| [C++](./C++/singleton.cpp) [Python](./Python/singleton.py) | _O(1)_ | _O(1)_ | Easy | | |
|208|[Assignment Operator Overloading (C++ Only)](http://lintcode.com/en/problem/assignment-operator-overloading-c-only/)| [C++](./C++/assignment-operator-overloading-c-only.cpp)| _O(n)_ | _O(1)_ | Medium | | |
|496|[Toy Factory](http://www.lintcode.com/en/problem/toy-factory/)| [C++](./C++/toy-factory.cpp) [Python](./Python/toy-factory.py) | _O(1)_ | _O(1)_ | Easy | | |
|497|[Shape Factory](http://www.lintcode.com/en/problem/shape-factory/)| [C++](./C++/shape-factory.cpp) [Python](./Python/shape-factory.py) | _O(1)_ | _O(1)_ | Easy | | |
|498|[Parking Lot](http://www.lintcode.com/en/problem/parking-lot/)| [C++](./C++/parking-lot.cpp) [Python](./Python/parking-lot.py) [Java](./Java/parking-lot.java) | _O(n * m * k)_ | _O(n * m * k)_ | Hard | CTCI | OO Design |
|708|[Elevator System OO Design](https://www.lintcode.com/problem/elevator-system-oo-design/)| [Python](./Python/elevator-system-oo-design.py) [C++](./C++/elevator-system-oo-design.cpp) [Java](./Java/elevator-system-oo-design.java) | | | Hard | | OO Design |
|709|[Restaurant OO Design](https://www.lintcode.com/problem/restaurant-oo-design/)| [C++](./C++/restaurant-oo-design.cpp) [Java](./Java/restaurant-oo-design.java) | | | Hard | | OO Design |
|710|[Hotel OO Design](https://www.lintcode.com/problem/hotel-oo-design/)| [C++](./C++/hotel-oo-design.cpp) [Java](./Java/hotel-oo-design.java) | | | Hard | | OO Design |
|712|[Vending Machine OO Design](https://www.lintcode.com/problem/vending-machine-oo-design/)| [C++](./C++/vending-machine-oo-design.cpp) [Java](./Java/vending-machine-oo-design.java) | | | Medium | | OO Design |
|714|[Black Jack OO Design](https://www.lintcode.com/problem/black-jack-oo-design/)| [C++](./C++/black-jack-oo-design.cpp) [Java](./Java/black-jack-oo-design.java) | | | Medium | | OO Design |
|731|[Restaurant II OO Design](https://www.lintcode.com/problem/restaurant-ii-oo-design/)| [C++](./C++/restaurant-ii-oo-design.cpp) [Java](./Java/restaurant-ii-oo-design.java) | | | Hard | | OO Design |
|732|[Hotel II OO Design](https://www.lintcode.com/problem/hotel-ii-oo-design/)| [C++](./C++/hotel-ii-oo-design.cpp) [Java](./Java/hotel-ii-oo-design.java) | | | Hard | | OO Design |
|746|[Tic Tac Toe OO Design](https://www.lintcode.com/problem/tic-tac-toe-oo-design/)| [C++](./C++/tic-tac-toe-oo-design.cpp) [Java](./Java/tic-tac-toe-oo-design.java) [Python](./Python/tic-tac-toe-oo-design.py) | | | Hard | | OO Design |
|747|[Coffee Maker OO Design](https://www.lintcode.com/problem/coffee-maker-oo-design/)| [C++](./C++/coffee-maker-oo-design.cpp) [Java](./Java/coffee-maker-oo-design.java) | | | Medium | | OO Design, decorator |
|748|[Kindle OO Design](https://www.lintcode.com/problem/kindle-oo-design/)| [C++](./C++/kindle-oo-design.cpp) [Java](./Java/kindle-oo-design.java) | | | Easy | | OO Design, factory |

## System Design
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|Sys1|News Feed System| | | | | | |
|501|[Mini Twitter](http://www.lintcode.com/en/problem/mini-twitter/)| [C++](./C++/mini-twitter.cpp) [Python](./Python/design-twitter.py) | _O(klogu)_ | _O(t + f)_ | Medium | | Heap |
|560|[Friendship Service](http://www.lintcode.com/en/problem/friendship-service/)| [Python](./Python/friendship-service.py) | | | Easy | | Hash |
|Sys2|Database and Cache| | | | | | |
|519|[Consistent Hashing](http://www.lintcode.com/en/problem/consistent-hashing/)| [Python](./Python/consistent-hashing.py) | _O(nlogn)_ | _O(n)_ | Easy | | Heap |
|520|[Consistent Hashing II](http://www.lintcode.com/en/problem/consistent-hashing-ii/)| [Python](./Python/consistent-hashing-ii.py) | | | Medium | | bisect, random |
|538|[Memcache](http://www.lintcode.com/en/problem/memcache/)| [Python](./Python/memcache.py) | | | Easy | | Hash |
|502|[mini-cassandra](http://www.lintcode.com/en/problem/mini-cassandra/)| [Python](./Python/mni-cassandraemcache.py) | | | Easy | | Hash |
|134|[LRU Cache](http://www.lintcode.com/en/problem/lru-cache/)| [Python](./Python/lru-cache.py) | _O(1)_ | _O(k)_ | Hard | | OrderedDict, Doubly LinkedList + Hash |
|24|[LFU Cache](http://www.lintcode.com/en/problem/lfu-cache/)| [Python](./Python/lfu-cache.py) | _O(1)_ | _O(k)_ | Hard | | Doubly LinkedList + Hash |
|Sys3|Tiny URL| | | | | | |
|232|[Tiny Url](https://lintcode.com/problem/tiny-url/description)| [Python](./Python/tiny-url.py) | | | Easy| | Hash, Dict |
|522|[Tiny Url II](https://lintcode.com/problem/tiny-url-ii/description)| [Python](./Python/tiny-url-ii.py) | | | Medium | |  Hash, Dict |
|526|[Load Balancer](https://lintcode.com/problem/load-balancer/description)| [Python](./Python/load-balancer.py) | | | Easy | |  Set, random |
|Sys4|Location Based Service| | | | | | |
|529|[Geohash](https://lintcode.com/problem/geohash/description)| [Python](./Python/geohash.py) | | | Medium | |  Geohash |
|530|[Geohash II](https://lintcode.com/problem/geohash-ii/description)| [Python](./Python/geohash-ii.py) | | | Medium | |  Geohash |
|525|[Mini Uber](https://lintcode.com/problem/mini-uber/description)| [Python](./Python/mini-uber.py) | | | Medium | | |
|509|[Mini Yelp](https://lintcode.com/problem/mini-yelp/description)| [Python](./Python/mini-yelp.py) | | | Hard | | Geohash, Bisect |
|Sys5|Web Crawler and Google Suggestion| | | | | | |
|500|[Inverted Index](https://lintcode.com/problem/inverted-index/description)| [Python](./Python/inverted-index.py) | | | Easy | | |
|523|[Url Parser](https://lintcode.com/problem/url-parser/description)| [Python](./Python/url-parser.py) | | | Hard | | Regex |
|442|[Implement Trie (Prefix Tree)](https://lintcode.com/problem/implement-trie-prefix-tree/description)| [Python](./Python/implement-trie-prefix-tree.py) | | | Medium | | Trie |
|559|[Trie Service](https://lintcode.com/problem/trie-service/description)| [Python](./Python/trie-service.py) | | | Medium | | Trie |
|527|[Trie Serializatioin](https://lintcode.com/problem/trie-serialization/description)| [Python](./Python/trie-serialization.py) | | | Hard | | Trie, Stack |
|231|[Typeahead](https://lintcode.com/problem/typeahead/description)| [Python](./Python/typeahead.py) | | | Medium | | Set |
|234|[Webpage Crawler](https://lintcode.com/problem/webpage-crawler/description)| [Python](./Python/webpage-crawler.py) | | | Hard | | Thread |
|Sys6|Distributed File System| | | | | | |
|566|[GFS Client](https://lintcode.com/problem/gfs-client/description)| [Python](./Python/gfs-cilent.py) | | | Easy | | |
|565|[Heart Beat](https://lintcode.com/problem/heart-beat/description)| [Python](./Python/heart-beat.py) | | | Easy | | |
|Sys7|Map Reduce| | | | | | |
|499|[Word Count (Map Reduce)](https://lintcode.com/problem/word-count-map-reduce/description)| [Python](./Python/word-count-map-reduce.py) | | | Easy | | |
|549|[Top K Frequent Words (Map Reduce)](https://lintcode.com/problem/top-k-frequent-words-map-reduce/description)| [C++](./C++/top-k-frequent-words-map-reduce.cpp) | | | Medium | | |
|503|[Anagram (Map Reduce)](https://lintcode.com/problem/anagram-map-reduce/description)| [Python](./Python/anagram-map-reduce.py) | | | Easy | | |
|504|[Inverted Index (Map Reduce)](https://lintcode.com/problem/inverted-index-map-reduce/description)| [Python](./Python/inverted-index-map-reduce.py) | | | Easy | | |
|654|[Sparse Matrix Multiplication](https://lintcode.com/problem/sparse-matrix-multiplication/description)| [Python](./Python/sparse-matrix-multiplication.py) | | | Easy | | |
|Sys8|Bigtable| | | | | | |
|556|[Standard Bloom Filter](https://lintcode.com/problem/standard-bloom-filter/description)| [Python](./Python/standard-bloom-filter.py) | | | Medium | | Hash |
|555|[Counting Bloom Filter](https://lintcode.com/problem/counting-bloom-filter/description)| [Python](./Python/counting-bloom-filter.py) | | | Medium | | Hash |
|486|[Merge K Sorted Arrays](https://lintcode.com/problem/merge-k-sorted-arrays/description)| [Python](./Python/merge-k-sorted-arrays.py) | | | Easy | | Heap |
|Sys9|Message System, Rate Limiter and Design Pattern| | | | | | |
|505|[Web logger](https://lintcode.com/problem/web-logger/description)| [Python](./Python/web-logger.py) | | | Easy | | |
|215|[Rate Limiter](https://lintcode.com/problem/rate-limiter/description)| [Python](./Python/rate-limiter.py) | | | Hard | | Bisect |
