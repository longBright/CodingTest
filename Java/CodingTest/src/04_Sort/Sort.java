public class Sort {
    public static void main(String[] args) {
        int[] arr1 = {7,5,9,0,3,1,6,2,4,8};
        selectionSort(arr1);

        int[] arr2 = {7,5,9,0,3,1,6,2,4,8};
        insertionSort(arr2);

        int[] arr3 = {7,5,9,0,3,1,6,2,4,8};
        quickSort(arr3, 0, arr3.length-1);
        printArray(arr3);

        int[] arr4 = {7,5,9,0,3,1,6,2,9,1,4,8,0,5,2};
        countSort(arr4);
    }

    // 선택 정렬
    public static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int minIdx = i;
            for (int j = i+1; j < arr.length; j++) {
                if (arr[minIdx] > arr[j]) {
                    minIdx = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = temp;
        }
        StringBuilder sb = new StringBuilder();
        for (int n: arr) {
            sb.append(n).append(" ");
        }
        System.out.println(sb);
    }

    // 삽입 정렬
    public static void insertionSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = i; j > 0; j--) {
                if (arr[j] < arr[j-1]) {
                    int temp = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = temp;
                }
                else {
                    break;
                }
            }
        }
        printArray(arr);
    }

    // 퀵 정렬
    public static void quickSort(int[] arr, int start, int end) {
        // 원소가 1개인 경우 종료
        if (start >= end) {
            return;
        }
        int pivot = start;      // 피벗 = 첫번째 원소
        int left = start + 1;
        int right = end;

        while(left <= right) {
            // 피벗보다 큰 데이터를 찾을 때까지 반복
            while(left <= end && arr[left] <= arr[pivot]) {
                left++;
            }
            // 피벗보다 작은 데이터를 찾을 때까지 반복
            while (right > start && arr[right] >= arr[pivot]) {
                right--;
            }
            // 엇갈렸다면 작은 데이터와 피벗을 교체
            if (left > right) {
                int temp = arr[right];
                arr[right] = arr[pivot];
                arr[pivot] = temp;
            }
            // 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            else {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
            }
        }
        // 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quickSort(arr, start, right - 1);
        quickSort(arr, right + 1, end);
    }

    // 계수 정렬
    public static void countSort(int[] arr) {
        int maxVal = 9;
        int[] count = new int[maxVal + 1];

        for (int i = 0; i < arr.length; i++) {
            count[arr[i]]++;
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= maxVal; i++) {
            for (int j = 0; j < count[i]; j++) {
                sb.append(i).append(" ");
            }
        }
        System.out.println(sb);
    }

    // 출력 메소드
    public static void printArray(int[] arr) {
        StringBuilder sb = new StringBuilder();
        for (int n: arr) {
            sb.append(n).append(" ");
        }
        System.out.println(sb);
    }
}
