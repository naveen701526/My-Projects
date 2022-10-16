class Solution {
    public static int[][] floodFill(int[][] image, int sr, int sc, int color) {
    if (sr > image.length && sc > image[0].length) return image;
    if (image[sr][sc] == color) return image;
	
    flood(image, sr, sc, color);
	
    return image;
}

private static void flood(int[][] image, int sr, int sc, int color) {
    int oldColor = image[sr][sc];
    image[sr][sc] = color;
	
    if (sr < image.length - 1 && oldColor == image[sr + 1][sc]) {
        flood(image, sr + 1, sc, color);
    }
	
    if (sr > 0 && oldColor == image[sr - 1][sc]) {
        flood(image, sr - 1, sc, color);
    }
	
    if (sc < image[sr].length - 1 && oldColor == image[sr][sc + 1]) {
        flood(image, sr, sc + 1, color);
    }
	
    if (sc > 0 && oldColor == image[sr][sc - 1]) {
        flood(image, sr, sc - 1, color);
    }
}
}
