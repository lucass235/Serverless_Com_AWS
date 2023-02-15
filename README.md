# serverless_com_AWS

## Como usar o serverless framework com AWS

### Instalação e configuração do AWS CLI

1. Instale o AWS CLI

```bash
pip install awscli
```

2. Configure o AWS CLI

```bash
aws configure
```

3. Digite as credenciais da sua conta AWS

```bash
AWS Access Key ID [None]: AAAAAAAAAAAAAAAAAAA
AWS Secret Access Key [None]: bbbbBBBBbbbBBBbbbBBBBbBB
Default region name [None]: us-west-2
Default output format [None]: ENTER
```

### Instalação e configuração do Serverless Framework

1. Instale o Serverless Framework

```bash
npm install -g serverless
```

2. Configure o Serverless Framework

```bash
serverless config credentials --provider aws --key AKIAIOSFODNN7EXAMPLE --secret wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

### Criando um projeto

1. Crie um projeto

```bash
serverless create --templete python3.8 --path my-service
```

2. Entre no diretório do projeto

```bash
cd my-service
```

3. faça o deploy

```bash
serverless deploy
```

4. teste o projeto

```bash
serverless invoke --function hello
```

### para remover o projeto

```bash
serverless remove
```

### Referências

- [Serverless Framework](https://www.serverless.com/)
- [Serverless Framework AWS](https://www.serverless.com/framework/docs/providers/aws/guide/quick-start/)
- [AWS](https://aws.amazon.com/pt/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
