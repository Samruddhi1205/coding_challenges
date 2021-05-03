#include<stdio.h>
int main()
{
    int i,n,count=0;
    scanf("%d",&n);
    int a[n];
    for (i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        if(a[i]==0)
        {
            count++;
        }
    }
    for(i=0;i<count;i++)
    {
        a[i]=0;
    }
    for(i=count;i<n;i++)
    {
        a[i]=1;
    }
    for(i=0;i<n;i++)
    {
        printf("%d",a[i]);
    }
}
