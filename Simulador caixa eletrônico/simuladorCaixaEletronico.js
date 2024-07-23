let saldo = 0;

      while (true) {
        let opcao = Number(
          prompt(`1- Ver saldo\n 2- Sacar \n 3- Depositar \n 4- Sair`)
        );

        if (opcao == 1) {
          alert(saldo);
        } else if (opcao == 2) {
          const valorSaque = Number(
            prompt("Digite o valor que gostaria de sacar: ")
          );
          if (valorSaque > saldo) {
            alert("Você não tem esse valor na sua conta! ");
          } else {
            saldo -= valorSaque;
            alert(`Foi sacado R$${valorSaque}. Você ainda tem R$${saldo}`);
          }
        } else if (opcao == 3) {
          const depositar = Number(
            prompt("Digite o valor que gostaria de depositar: ")
          );
          saldo += depositar;
          alert(`Deposito efetuado com sucesso! Novo saldo: R$${saldo}`);
        } else {
          alert("Até a próxima!");
          break;
        }
      }