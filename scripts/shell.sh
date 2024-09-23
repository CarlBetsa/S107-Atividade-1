# Variáveis de ambiente recebidas do GitHub Actions
RECIPIENT_EMAIL="$RECIPIENT_EMAIL"
RECIPIENT_EMAIL2="$RECIPIENT_EMAIL2"

sudo apt-get install mailutils

# Verifica se as variáveis necessárias estão presentes
if [[ -z "$RECIPIENT_EMAIL" && -z "$RECIPIENT_EMAIL2" ]]; then
  echo "Faltando variáveis de ambiente. Verifique RECIPIENT_EMAIL."
  exit 1
fi

# Conteúdo do e-mail
SUBJECT="Notificação: Execução do Pipeline"
BODY="Pipeline executado com sucesso!"

# Enviando o e-mail usando o comando sendmail
echo -e "Subject:${SUBJECT}\n\n${BODY}" | sendmail -v "$RECIPIENT_EMAIL"
echo -e "Subject:${SUBJECT}\n\n${BODY}" | sendmail -v "$RECIPIENT_EMAIL2"
