#include <stdio.h>
#include <stdlib.h>
int main()
{
    setbuf(stdout, NULL);
    int con;
    con = 0;
    int account_balance = 1100;
    while(con == 0){
        
        printf("Welcome to Void's Secret Market\n");
        printf("Here we sell flags and nothing more!\n");

        printf("\n1. Check current balance\n");
        printf("2. Buy flags\n");
        printf("3. Exit\n");
        int menu;
        printf("\nChoose an option: ");
        fflush(stdin);
        scanf("%d", &menu);
        if(menu == 1){
            printf("\nBalance: %d \n\n", account_balance);
        }
        else if(menu == 2){
            printf("\nCurrently selling:\n");
            printf("1. Dirty flag\n");
            printf("2. Void's flag\n");
            int auction_choice;
            printf("\nChooose an option: ");
            fflush(stdin);
            scanf("%d", &auction_choice);
            if(auction_choice == 1){
                printf("\nThese smelly flags cost 900 each, how many do you want? ");
                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if(number_flags > 0){
                    int total_cost = 0;
                    total_cost = 900*number_flags;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nThis is your balance after the purchase: %d\n\n", account_balance);
                    }
                    else{
                        printf("\nYou don't have enough funds to make this purchase!\n\n");
                    }   
                } 
            }
            else if(auction_choice == 2){
                printf("\nVoid's flag costs 100000, and we only have 1 in stock!\n");
                printf("Type '1' to buy one: ");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);
                if(bid == 1){
                    if(account_balance > 100000){
                        FILE *f = fopen("flag.txt", "r");
                        if(f == NULL){

                            printf("\nFlag not found, run the program on the server...\n");
                            exit(0);
                        }
                        char buf[64];
                        fgets(buf, 63, f);
                        printf("\nThe flag is: %s\n", buf);
                        }
                    else{
                        printf("\nYou don't have enough funds to make this purchase!\n\n");
                    }
                }
            }
        }
        else{
            con = 1;
        }
    }
    return 0;
}
