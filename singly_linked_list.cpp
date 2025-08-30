#include<stdio.h>
#include<stdlib.h>
int num,pos,val;
struct node
{
	int info;
	struct node *next;
};
struct node *head=NULL;
void create()
{
	struct node*temp,*ptr;
	temp=(struct node*)malloc(sizeof(struct node));
	if(temp==NULL)
	{
		printf("Memory not available");
		return;
	}
	
		printf("Enter the data: ");
		scanf("%d",&temp->info);
		temp->next=NULL;
		if(head==NULL)
		{
			head=temp;
		}
		else
		{
			ptr=head;
		while(ptr->next!=NULL)
		{
			ptr=ptr->next;
		}
		ptr->next=temp;
		}
}
void add_beg(int num)
{
	struct node *temp;
	temp=(struct node*)malloc(sizeof(struct node));
	printf("Enter the data");
	scanf("%d",&num);
	temp->info=num;
	temp->next=head;
	head=temp;
	
}
void add_middle(int num , int pos)
{
	struct node*temp,*q;
	int i;
	temp=(struct node*)malloc(sizeof(struct node));
	printf("Enter the data");
	scanf("%d",&num);
	temp->next=NULL;
	printf("Enter the position");
	scanf("%d",&pos);
	temp->info=num;
	if(pos==0)
	{
		q=head;
	temp->next=head;
	
	head=temp;
	}
	else
	{
		q=head;
	for(i=0;i<pos-1;i++)
	{
		q=q->next;
		if(pos==NULL)
		{
			printf("Position not found");
			return;
		}
	}
	temp->next=q->next;
	q->next=temp;
}
}
void add_end(int num)
{
	struct node*temp;
	temp=(struct node*)malloc(sizeof(struct node));
	struct node*q=head;
	printf("Enter the data");
	scanf("%d",&num);
	while(q->next!=NULL)
	{
		q=q->next;
	}
	q->next=temp;
}
void display()
{
	struct node*ptr;
	if(head==NULL)
	{
		printf("Linked list is empty");
		return;
	}
	else
	{
		ptr=head;
		while(ptr!=NULL)
		{
		
			printf("%d\t",ptr->info);
			ptr=ptr->next;
		}
	
	}
}
void del_beg()
{
	struct node *ptr;
	ptr=(struct node*)malloc(sizeof(struct node));
	if(head==NULL)
	{
		printf("The list is underflow");
		return;
	}
	else
	{
		ptr=head;
		head=head->next;
		printf("The deleted element is %d",ptr->info);
		free(ptr);
	}
}
void del_end()
{
	struct node*ptr,*temp;
	if(head==NULL)
	{
		printf("The linked list is underflow");
		return;
	}
	else if(head->next==NULL)
	{
		ptr=head;
		head=NULL;
		free(ptr);
	}
	else
	{
		ptr=head;
		while(ptr->next!=NULL)
		{
			temp=ptr;
			ptr=ptr->next;
		}
			temp->next=NULL;
			printf("The deleted element is %d",ptr->info);
			free(ptr);
	}
}
void del_after()
{
	struct node*ptr,*temp;
	int i;
	if(head==NULL)
	{
		printf("The linked list is underflow");
		return;
	}
	else
	{
		printf("Enter the position: ");
		scanf("%d",&pos);
		if(pos==0)
		{
		ptr=head;
		head=head->next;
		printf("The deleted element is %d",ptr->info);
		free(ptr);
		}
		else
		{
			ptr=head;
			for(i=0;i<pos;i++)
			{
				temp=ptr;
				ptr=ptr->next;
				if(ptr==NULL)
				{
					printf("The position is not found");
				}
				else
				{
					temp->next=ptr->next;
				}
			}
			printf("The deleted element is %d",ptr->info);
					free(ptr);
		}
	}
}
void reverse()
{
	struct node*p1,*p2,*p3;
	if(head->next==NULL)
	{
		return;
	}
	else
	{
		p1=head;
		p2=p1->next;
		p3=p2->next;
		p2->next=p1;
		p1->next=NULL;
		while(p3!=NULL)
		{
			p1=p2;
			p2=p3;
			p3=p3->next;
			p2->next=p1;
		}
		head=p2;
	}
}
void search(int val)
{
	int pos=1;
	struct node*ptr;
	ptr=head;
	while(ptr!=NULL)
	{
	if(ptr->info==val)
		{
		printf("The element is found in position %d",pos);
		return;
	    }
	    ptr=ptr->next;
		pos++;
	}
	if(ptr==NULL)
	
	{
		printf("The element is not found");
	}
}
void count()
{
	int count=0;
	struct node*ptr;
	ptr=head;
	while(ptr!=NULL)
	{
		ptr=ptr->next;
		count++;
	}
	printf("The number of elements in linked list are %d",count);
}
int main()
{
	int opt;
		while(1)
		{
		printf("\n1.Create\n2.Display\n3.Insert at start\n4.Insert at middle\n5.Insert at end\n6.Delete at start\n7.Delete at end\n8.Delete after\n9.Reverse\n10.Search\n11.Count\n12.Exit\n");
	printf("Enter the option: ");
	scanf("%d",&opt);
	{
	switch(opt)
	{
		case 1:
			{
			    create();
				break;
			}
		case 2:
			{
				display();
				break;
			}
		case 3:
			{
				add_beg(num);
				break;
			}
		case 4:
			{
				add_middle(num,pos);
				break;
			}
		case 5:
			{
				add_end(num);
				break;
			}
		case 6:
			{
				del_beg();
				break;
			}
		case 7:
			{
				del_end();
				break;
			}
		case 8:
			{
				del_after();
				break;
			}
			case 9:
			{
				reverse();
				break;
			}
			case 10:
			{
				printf("Enter the value");
				scanf("%d",&val);
				search(val);
				break;
			}
			case 11:
			{
				count();
				break;
			}
			case 12:
			{
				exit(0);
			}
		default:
			{
				printf("Incorrect option");
			}
		
	}
}
}
return 0;
}
