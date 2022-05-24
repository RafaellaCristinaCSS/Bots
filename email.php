<?php
$para = "rafacssacrament@gmail.com";
$assunto = "Promessa é Divida!";
$corpo = "O Programa para enviar emails ja esta funcionando!;";
$headers = "from:danielsilveriocorretorls@gmail.com";

if(mail($para, $assunto, $corpo, $headers)){
    echo "Email enviado para $para com sucesso;"
}else {
    echo "Falha no envio do email";
}
?>