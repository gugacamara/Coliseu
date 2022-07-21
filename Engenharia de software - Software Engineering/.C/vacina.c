#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <string.h>

/*OBS! código funcionando normalmente no VScode mas não no Replit*/

/*menu de controle do usuário*/
int menu(int controle)
{
int escolha;

printf("\nSeja bem vindo.\nDigite um valor para proseguir; \n1 - Cadastrar Vacina. \n2 - Listar Aplicações. \n3 - Consultar por CPF. \n4 - Sair. \n");
scanf("%d", &escolha);
fflush(stdin);

return escolha;
}

/*informações do usuário*/
struct vacina
{
    int codigo;
    char nome[300];
    char cpf[300];
    char vacinaAp[300];
    char dataAp[300];
    int numLote;

};

/*inicio da função principal*/
int main(){

/*habilitação da acentuação*/
setlocale(LC_ALL, "Portuguese");

/*declaração de variáveis*/
int controle = 0, controle2, i = 0, g, c, j;
char cpf2[300];

/*declaração da struct*/
struct vacina vacinados[99]; 

controle = menu(controle);

while (controle != 4)
{

switch (controle)
{

/*leitura dos dados do usuário*/
case 1:

vacinados[i].codigo = i;

printf("\nDigite seu nome.\n");
gets(vacinados[i].nome);
fflush(stdin);

printf("Digite o seu CPF.\n");
scanf("%s", vacinados[i].cpf);
fflush(stdin);

printf("Digite a vacina aplicada.\n");
scanf("%s", &vacinados[i].vacinaAp);
fflush(stdin);

printf("Digite a data de aplicação.\n");
scanf("%s", &vacinados[i].dataAp);
fflush(stdin);

printf("Digite o número do lote da vacina.\n");
scanf("%d", &vacinados[i].numLote);
fflush(stdin);

system("cls");

printf("\nCadastro efetuado com sucesso!\n");

i++;

controle = menu(controle);

break;

/*lista dos dados registrados na struct*/   
case 2:

system("cls");

    for (g=0; g<i; g++){

printf("\nCódigo: %d \n", vacinados[g].codigo);
printf("Nome: %s \n", vacinados[g].nome);
printf("CPF: %s \n", vacinados[g].cpf);
printf("Vacina: %s \n", vacinados[g].vacinaAp);
printf("data: %s \n", vacinados[g].dataAp);
printf("Numero do lote: %d \n", vacinados[g].numLote);
printf("==========================================\n");

}

controle = menu(controle);

break;

/*Consulta do CPF pelo usuário*/
case 3:

system("cls");

printf("\nDigite o CPF que deseja pesquisar.\n");
scanf("%s", &cpf2);
fflush(stdin);

controle2 = 1;

    for (c=0; c<i; c++){

if(strcmp(cpf2, vacinados[c].cpf) == 0)
{
system("cls");
printf("\nCPF encontrado!\n\n");
printf("Código: %d \n", vacinados[c].codigo);
printf("Nome: %s \n", vacinados[c].nome);
printf("CPF: %s \n", vacinados[c].cpf);
printf("Vacina: %s \n", vacinados[c].vacinaAp);
printf("data: %s \n", vacinados[c].dataAp);
printf("Numero do lote: %d \n", vacinados[c].numLote);
printf("==========================================\n");

controle2 = 2;

}

}

/*controle para a mensagem aparecer uma unica vez*/
if(controle2 == 1)
{
 system("cls");
 printf("\nCPF não encontrado!\n");
}

controle = menu(controle);

break;

case 4:

/*Programa encerrado*/

break;

default:
system("cls");
printf("\nComando inválido!\n");
controle = menu(controle);

break;

}

}

return (0);



}

