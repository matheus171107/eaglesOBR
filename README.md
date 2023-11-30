# BIBLIOTECA "EaglesMotors" - para Arduino
<p>Biblioteca feita totalmente pela equipe SESI Eagles, ela funciona controlando motores DC, utilizando módulos de Ponte H</p>

<div>
    <h2>Inicialização da biblioteca</h2>
    <p>
        Para começar a utilizar, você terá que defenir os motores, passando como parâmetros: <code>int pinForward, pinBackward, pinVelocity</code>, como no exemplo a seguir:
    </p>
    <p>
        <code>#define pinForward 7</code><br>
        <code>#define pinBackward 6</code><br>
        <code>#define pinVelocity 5</code><br>
        <br>
        <code>EaglesMotors MOTOR_NAME_1(pinForward, pinBackward, pinVelocity);</code> 
    </p>
    <br>
    <p>
        Você também pode fazer o mesmo para dois motores: 
    </p>
    <p>
        <code>EaglesMotors MOTOR_NAME_1(pinForward1, pinBackward1, pinVelocity1);</code><br>
        <code>EaglesMotors MOTOR_NAME_2(pinForward2, pinBackward2, pinVelocity2);</code>
    </p>
    <br>
    <p>
        Após, será necessário setar todos os pinos como saída em <code>void setup()</code> :
    </p>
    <p> 
        <code>pinMode(pinForward, OUTPUT);</code><br>
        <code>pinMode(pinBackward, OUTPUT);</code><br>
        <code>pinMode(pinVelocity, OUTPUT);</code>
    </p>
</div>
<br><br>
<div>
    <h2>Método <code>.setMoviment()</code> :</h2>
    <p>
        Este método é utilizado para definir o sentido do movimento e a velocidade do motor. Para utilizá-lo será necessário passar dois parâmetros: <code>.setMoviment(char sense, int velocity)</code>
    </p>
    <div>
        <h3>Palavras-chaves presentes</h3>
        <ul>
          <li><code>"F"</code> - do tipo <code>Char</code>, é utilizada para indicar sentido horário ou <code>FORWARD</code></li>
          <li><code>"B"</code> - do tipo <code>Char</code>, é utilizada para indicar sentido anti-horário ou <code>BACKWARD</code></li>
          <li><code>"R"</code> - do tipo <code>Char</code>, é utilizada para indicar sentido de parar ou <code>RELEASE</code></li>
        </ul>
    </div>
    <div>
        <h3>Exemplos: </h3>
        O código abaixo irá fazer os motores rotacionarem no sentido horário com velocidade 200: <br>
        <code>MOTOR_NAME_1.setMoviment("F", 200);</code> <br><br>
        Isso irá fazer os motores rotacionarem no sentido anti-horário com velocidade 100: <br>
        <code>MOTOR_NAME_1.setMoviment("B", 100);</code> <br><br>
        Este fará os motores parar: <br>
        <code>MOTOR_NAME_1.setMoviment("R", 0);</code> <br><br>
    </div>
</div>
<br><br>
<div>
    <h2>Método <code>.setSpeed()</code> :</h2>
    <p>
        Este método é utilizado para definir a velocidade do motor. Para utilizá-lo será necessário passar um parâmetro: <code>.setSpeed(int velocity)</code>
    </p>
    <div>
        <h3>Exemplos: </h3>
        O código abaixo irá fazer os motores rotacionarem com velocidade 200: <br>
        <code>MOTOR_NAME_1.setSpeed(200);</code> <br><br>
        Isso irá fazer os motores rotacionarem com velocidade 100: <br>
        <code>MOTOR_NAME_1.setSpeed(100);</code> <br><br>
        Este fará os motores parar: <br>
        <code>MOTOR_NAME_1.setSpeed(0);</code> <br><br>
    </div>
</div>
<br><br>
<div>
    <h2>Método <code>.run()</code> :</h2>
    <p>
        Este método é utilizado para definir o sentido do movimento. Para utilizá-lo será necessário passar um parâmetro: <code>.run(char sense)</code>
    </p>
    <div>
        <h3>Exemplos: </h3>
        O código abaixo irá fazer os motores rotacionarem no sentido horário: <br>
        <code>MOTOR_NAME_1.run("F");</code> <br><br>
        Isso irá fazer os motores rotacionarem no sentido anti-horário: <br>
        <code>MOTOR_NAME_1.run("B");</code> <br><br>
        Este fará os motores parar: <br>
        <code>MOTOR_NAME_1.run("R");</code> <br><br>
    </div>
</div>

