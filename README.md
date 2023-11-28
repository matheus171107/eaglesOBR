# BIBLIOTECA "EaglesMotors"
<p>Biblioteca feita totalmente pela equipe SESI Eagles, elas funciona como um controlador de motores DC, utilizando módulos de Ponte H</p>

<div>
  <h3>Palavras-chaves presentes</h3>
  <ul>
      <li><code>"F"</code> - do tipo <code>Char</code>, é utilizada para indicar sentido de frente ou <code>FORWARD</code></li>
      <li><code>"B"</code> - do tipo <code>Char</code>, é utilizada para indicar sentido de trás ou <code>BACKWARD</code></li>
      <li><code>"R"</code> - do tipo <code>Char</code>, é utilizada para indicar sentido de parar ou <code>RELEASE</code></li>
    </ul>
</div>
<div>
    <h3>Inicialização da biblioteca</h3>
    <p>
        Para começar a utilizar, você terá que defenir os motores, passando como parâmetros: <code>int pinForward, pinBackward, pinVelocity</code>, como no exemplo a seguir:
    </p>
    <code>
        #define pinForward 7  <br>
        #define pinBackward 6 <br>
        #define pinVelocity 5 <br>
        <br>
        EaglesMotors MOTOR_NAME_1(pinForward, pinBackward, pinVelocity); 
    </code>
    <p>
        Você também pode fazer o mesmo para dois motores: 
    </p>
    <code>
        EaglesMotors MOTOR_NAME_1(pinForward1, pinBackward1, pinVelocity1);<br>
        EaglesMotors MOTOR_NAME_2(pinForward2, pinBackward2, pinVelocity2); 
    </code>
</div>
