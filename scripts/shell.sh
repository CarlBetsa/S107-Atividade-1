# Variáveis de ambiente recebidas do GitHub Actions
EMAIL_RECIPIENT="$EMAIL_RECIPIENT"
EMAIL_RECIPIENT2="$EMAIL_RECIPIENT2"

sudo apt-get install mailutils


# Conteúdo do e-mail
SUBJECT="Notificação: Execução do Pipeline"
BODY="Pipeline executado com sucesso!"

# Enviando o e-mail usando o comando sendmail
echo -e "Subject:${SUBJECT}\n\n${BODY}" | sendmail -v "$EMAIL_RECIPIENT"
echo -e "Subject:${SUBJECT}\n\n${BODY}" | sendmail -v "$EMAIL_RECIPIENT2"
