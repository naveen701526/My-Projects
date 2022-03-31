class Solution {
    public int search(int[] nums, int target) {

        // Find the offset
        int offset = findOffset(nums, 0, nums.length - 1);

        int low = offset;
        int high = nums.length - 1 + offset;

        while (low <= high) {

            int mid = low + (high - low) / 2;

            if (nums[mid % nums.length] > target) {
                high = mid - 1;
            } else if (nums[mid % nums.length] < target) {
                low = mid + 1;
            } else {
                return mid % nums.length;
            }
        }

        return -1;
    }

    private int findOffset(int[] arr, int low, int high) {

        if (low < high) {

            int mid = low + (high - low) / 2;

            // 1, 2, 3
            if (arr[mid] > arr[low] && arr[mid] < arr[high]) {
                return findOffset(arr, low, mid - 1);
            }

            // 3, 1, 2
            if (arr[mid] < arr[low] && arr[mid] < arr[high]) {
                return findOffset(arr, low, mid);
            }

            // 2, 3, 1
            if (arr[mid] > arr[low] && arr[mid] > arr[high]) {
                return findOffset(arr, mid + 1, high);
            }

            // 2, 1
            // 1, 2
            return arr[mid] < arr[high] ? mid : high;
        }

        // 1
        return low;
    }
}
