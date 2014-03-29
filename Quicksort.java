package sorting;

// Adapted from open source: http://codereview.stackexchange.com/questions/4022/java-implementation-of-quick-sort
// improved pivot selection and stuff

public class Quicksort {

    /**
     * @param args
     */
    public static void main(String[] args) {
        int a[]={23,44,1,2009,2,88,123,7,999,1040,88};
        quickSort(a, 0, a.length - 1);
        System.out.println("dfd");
        for(int i=0; i<a.length; i++) {
        	System.out.print(a[i] + " ");
        }

    }

    public static void quickSort(int[] a, int p, int r)
    {
        if(p<r)
        {
        	int pivotLocation = medianOfThree(a, p, r);
            pivotLocation=partition(a,p,r, pivotLocation);
            quickSort(a,p,pivotLocation);
            quickSort(a,pivotLocation+1,r);
        }
    }
    
    public static int medianOfThree(int[] A, int left, int right) {
    	// bubble sort
    	int mid = (right - left)/2 + left;
    	if (A[left] < A[mid]) {
    		swap(A, left, mid);	
    	}
    	if (A[mid] < A[right]){
    		swap(A, mid, right);
    	}
    	if (A[left] < A[mid]) {
    		swap(A, left, mid);
    	}
    	return mid;
    }
    
    private static int partition(int[] a, int p, int r, int pivotLocation) {
        int x = a[pivotLocation];
        int i = p-1 ;
        int j = r+1 ;

        while (true) {
            i++;
            while ( i< r && a[i] < x)
                i++;
            j--;
            while (j>p && a[j] > x)
                j--;
            if (i < j)
                swap(a, i, j);
            else
                return j;
        }
    }

    private static void swap(int[] a, int i, int j) {
        // TODO Auto-generated method stub
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}

