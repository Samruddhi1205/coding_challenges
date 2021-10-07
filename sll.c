#include<stdio.h>  
#include<stdlib.h>  
struct node   
{  
    int data;  
    struct node *link;   
};  
struct node *head;  
  
void insert ();  
void delete();  
void display();  
void main ()  
{  
    int ch =0;  
    while(ch != 4)   
    {  
        printf("\n1.Insert\n2.Delete\n3.Display\n4.Exit\n");  
        printf("\nEnter your choice?\n");         
        scanf("\n%d",&ch);  
        switch(ch)  
        {  
            case 1:  
            insert();      
            break;  
            case 2:  
            delete();         
            break;  
            case 3:  
            display();       
            break;  
            case 4:  
            exit(0);  
            break;  
            default:  
            printf("Please enter valid choice..");  
        }  
    }  
}  
void insert()  
{  
    struct node *ptr,*temp;  
    int item;     
    ptr = (struct node*)malloc(sizeof(struct node));      
    if(ptr == NULL)  
    {  
        printf("\nOVERFLOW");     
    }  
    else  
    {  
        printf("\nEnter value?\n");  
        scanf("%d",&item);  
        ptr->data = item;  
        if(head == NULL)  
        {  
            ptr -> link = NULL;  
            head = ptr;  
        }  
        else  
        {  
            temp = head;  
            while (temp -> link != NULL)  
            {  
                temp = temp -> link;  
            }  
            temp->link = ptr;  
            ptr->link = NULL;  
        }  
    }  
}  
 
void delete()  
{  
    struct node *ptr,*ptr1;  
    if(head == NULL)  
    {  
        printf("\nlist is empty");  
    }  
    else if(head -> link == NULL)  
    {  
        head = NULL;  
        free(head);  
        printf("\nOnly node of the list deleted ...\n");  
    }  
          
    else  
    {  
        ptr = head;   
        while(ptr->link != NULL)  
        {  
            ptr1 = ptr;  
            ptr = ptr ->link;  
        }  
        ptr1->link = NULL;  
        free(ptr);  
        printf("\nDeleted Node from the last ...\n");  
    }     
}  
void display()  
{  
    struct node *ptr;  
    ptr = head;   
    if(ptr == NULL)  
    {  
        printf("Empty");  
    }  
    else  
    {  
        printf("\nlinked list data\n");   
        while (ptr!=NULL)  
        {  
            printf("\n%d",ptr->data);  
            ptr = ptr -> link;  
        }  
    }  
}  
