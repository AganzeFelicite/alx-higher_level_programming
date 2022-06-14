#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is palindrome
 *
 * @head: the first node of the linked list
 * Return: 1 if it's a palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	size_t num_nodes, half, i;
	listint_t *mid_node, *start, *new_begin;

	if (!head || !*head)
		return (1);

	num_nodes = list_len(*head);
	half = num_nodes % 2 == 0 ? (num_nodes / 2) : (num_nodes / 2) + 1;
	mid_node = start = *head;

	for (i = 0; i < half; i++)	/* get next node after middle */
		mid_node = mid_node->next;

	new_begin = reverse_listint(&mid_node);	/* reverse the node */
	if (num_nodes % 2 != 0)	/* check if node is odd */
		half -= 1;

	for (i = 0; i < half; i++)	/* traverse start node with reversed start */
	{
		if (start->n != new_begin->n)
			return (0);
		start = start->next;
		new_begin = new_begin->next;
	}
	return (1);
}

/**
 * list_len - gets the number of nodes in list
 *
 * @head: first node in list
 * Return: number of nodes in list or 0 if empty
 */
int list_len(const listint_t *head)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = head;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * reverse_listint - reverse the lists
 * @head: pointer to pointer to head
 * Return: head
 */

listint_t *reverse_listint(listint_t **head)
{
	/*declare variables to be used*/
	listint_t *prev, *current;
	/*check if head is not NULL*/
	if (*head == NULL)
		return (NULL);
	/*initialize pointers*/
	current = *head;
	prev = NULL;
	/*loop through and reverse the list by updating address*/
	while (*head != NULL)
	{
		/*set current to next address*/
		current = current->next;
		/*update the next address in node to previous*/
		(*head)->next = prev;
		/*set prev to the head address*/
		prev = *head;
		/*move head to the next address (current)*/
		*head = current;
	}
	/* head is NULL set it to the prev address*/
	*head = prev;
	return (*head);
}
