def p1():
    return """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:paddingLeft="20dp"
    android:paddingTop="25dp"
    android:paddingRight="20dp"
    tools:context=".MainActivity">

    <RelativeLayout
        android:layout_width="match_parent"
        android:layout_height="59dp">

        <TextView
            android:id="@+id/textView"
            android:layout_width="wrap_content"
            android:layout_height="44dp"
            android:layout_alignParentStart="true"
            android:layout_alignParentEnd="true"
            android:layout_alignParentBottom="true"
            android:layout_marginStart="98dp"
            android:layout_marginLeft="20dp"
            android:layout_marginEnd="103dp"
            android:layout_marginBottom="10dp"
            android:gravity="center"
            android:text="ITC INFOTECH LTD"
            android:textColor="#E61717"
            android:textSize="20sp" />

        <ImageView
            android:id="@+id/imageView4"
            android:layout_width="48dp"
            android:layout_height="match_parent"
            android:layout_alignParentBottom="true"
            android:layout_marginLeft="11dp"
            android:layout_marginBottom="0dp"
            android:layout_toRightOf="@id/textView"
            app:srcCompat="@drawable/one"
        />
    </RelativeLayout>

    <View
        android:layout_width="match_parent"
        android:layout_height="2dp"
        android:background="#000000" />

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="John Doe"
        android:textSize="16dp"
        android:layout_marginBottom="10dp"
        android:layout_marginTop="10dp"
        android:textColor="#000000"
        android:gravity="center" />

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Assosiate IT Consultant"
        android:textSize="16dp"
        android:layout_marginBottom="10dp"
        android:layout_marginTop="10dp"
        android:textColor="#000000"
        android:gravity="center" />

    <View
        android:layout_width="match_parent"
        android:layout_height="2dp"
        android:background="#000000" />

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="+91-9998887776"
        android:textSize="16dp"
        android:layout_marginBottom="10dp"
        android:layout_marginTop="10dp"
        android:textColor="#000000"
        android:gravity="center" />

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Bangalore"
        android:textSize="16dp"
        android:layout_marginBottom="10dp"
        android:layout_marginTop="10dp"
        android:textColor="#000000"
        android:gravity="center" />

    <TextView
        android:layout_marginTop="10dp"
        android:layout_marginBottom="10dp"
        android:gravity="center"
        android:text="Email:johndoe@gmail.com"
        android:textColor="#000000"
        android:textSize="16dp" />
</LinearLayout>
"""

def p2():
    return """<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="117dp"
        android:layout_marginBottom="532dp"
        android:text="Simple Calculator"
        android:textSize="24sp" />

    <EditText
        android:id="@+id/editText1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="95dp"
        android:layout_marginBottom="457dp"
        android:ems="10"
        android:hint="Enter the Number1"
        android:inputType="textPersonName"
        android:text="" />

    <EditText
        android:id="@+id/editText2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="95dp"
        android:layout_marginBottom="392dp"
        android:ems="10"
        android:hint="Enter the Number2"
        android:inputType="textPersonName"
        android:text="" />

    <TextView
        android:id="@+id/textView1"
        android:layout_width="129dp"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="123dp"
        android:layout_marginBottom="319dp"
        android:text="0"
        android:textSize="34sp" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="245dp"
        android:layout_marginBottom="243dp"
        android:onClick="add"
        android:text="ADD" />

    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="56dp"
        android:layout_marginBottom="243dp"
        android:onClick="Sub"
        android:text="SUB" />

    <Button
        android:id="@+id/button3"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="240dp"
        android:layout_marginBottom="170dp"
        android:onClick="mul"
        android:text="MUL" />

    <Button
        android:id="@+id/button4"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="53dp"
        android:layout_marginBottom="165dp"
        android:onClick="div"
        android:text="DIV" />
</RelativeLayout>
JAVA
package com.example.simplecalci;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    EditText e1,e2;
    TextView tv1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        e1=(EditText)findViewById(R.id.editText1);
        e2=(EditText)findViewById(R.id.editText2);
        tv1=(TextView)findViewById(R.id.textView1);
    }

    public void add(View view){
        int a1 = Integer.parseInt(e1.getText().toString());
        int a2 = Integer.parseInt(e2.getText().toString());
        int result= a1+a2;
        tv1.setText(""+result);
    }

    public void Sub(View view){
        int a1 = Integer.parseInt(e1.getText().toString());
        int a2 = Integer.parseInt(e2.getText().toString());
        int result= a1-a2;
        tv1.setText(""+result);
    }

    public void mul(View view){
        int a1 = Integer.parseInt(e1.getText().toString());
        int a2 = Integer.parseInt(e2.getText().toString());
        int result= a1*a2;
        tv1.setText(""+result);
    }

    public void div(View view){
        int a1 = Integer.parseInt(e1.getText().toString());
        int a2 = Integer.parseInt(e2.getText().toString());
        float result= a1/a2;
        tv1.setText(""+result);
    }
}
"""

def p3():
    return """signup activity<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="159dp"
        android:layout_marginBottom="540dp"
        android:text="Sign Up"
        android:textSize="34sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <EditText
        android:id="@+id/editTextEmail"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="106dp"
        android:layout_marginBottom="468dp"
        android:ems="10"
        android:hint="Email-id"
        android:inputType="textEmailAddress" />

    <EditText
        android:id="@+id/editTextPassword"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="93dp"
        android:layout_marginBottom="371dp"
        android:ems="10"
        android:hint="Enter Password"
        android:inputType="textPassword" />

    <Button
        android:id="@+id/signup"
        android:layout_width="wrap_content"
        android:onClick="signup"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="162dp"
        android:layout_marginBottom="260dp"
        android:text="Signup" />
</RelativeLayout>
signup JAVA
package com.example.loginapplication;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;
import java.util.regex.Pattern;

public class MainActivity extends AppCompatActivity {
    EditText emailText, passwordText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        emailText = findViewById(R.id.editTextEmail);
        passwordText = findViewById(R.id.editTextPassword);
    }

    public void signup(View view) {
        String email = emailText.getText().toString();
        String password = passwordText.getText().toString();
        if (!isValidPassword(password)) {
            Toast.makeText(this, "Password does not match rules", Toast.LENGTH_LONG).show();
            return;
        }
        Intent intent = new Intent(this, LoginActivity.class);
        intent.putExtra("email", email);
        intent.putExtra("password", password);
        startActivity(intent);
    }

    Pattern lowercase = Pattern.compile("^.*[a-z].*$");
    Pattern uppercase = Pattern.compile("^.*[A-Z].*$");
    Pattern number = Pattern.compile("^.*[0-9].*$");
    Pattern schar = Pattern.compile("^.*[^a-zA-Z0-9].*$");

    private Boolean isValidPassword(String password) {
        if (password.length() < 8) {
            return false;
        }
        if (!lowercase.matcher(password).matches()) {
            return false;
        }
        if (!uppercase.matcher(password).matches()) {
            return false;
        }
        if (!number.matcher(password).matches()) {
            return false;
        }
        if (!schar.matcher(password).matches()) {
            return false;
        }
        return true;
    }
}
login Activity
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".LoginActivity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="189dp"
        android:layout_marginBottom="602dp"
        android:text="Login"
        android:textSize="34sp" />

    <EditText
        android:id="@+id/editTextEmail"
        android:layout_width="187dp"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="111dp"
        android:layout_marginBottom="484dp"
        android:ems="10"
        android:hint="Email-id"
        android:inputType="textEmailAddress" />

    <EditText
        android:id="@+id/editTextPassword"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="98dp"
        android:layout_marginBottom="390dp"
        android:ems="10"
        android:hint="Enter password"
        android:inputType="textPassword" />

    <Button
        android:id="@+id/login"
        android:layout_width="wrap_content"
        android:onClick="login"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="148dp"
        android:layout_marginBottom="261dp"
        android:text="Login" />

</RelativeLayout>
Login JAVA
package com.example.loginapplication;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class LoginActivity extends AppCompatActivity {
    EditText emailText, passwordText;
    String rEmail, rPassword;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        emailText = findViewById(R.id.editTextEmail);
        passwordText = findViewById(R.id.editTextPassword);

        rEmail = getIntent().getStringExtra("email");
        rPassword = getIntent().getStringExtra("password");
    }

    public void login(View view) {
        String email = emailText.getText().toString();
        String password = passwordText.getText().toString();

        if (rEmail.equals(email) && rPassword.equals(password)) {
            Intent intent = new Intent(this, LoginSuccessful.class);
            startActivity(intent);
        } else {
            Toast.makeText(this, "Invalid Credentials", Toast.LENGTH_LONG).show();
        }
    }
}
Login Successful
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".LoginSuccesful">

    <TextView
        android:id="@+id/textView2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="78dp"
        android:layout_marginBottom="463dp"
        android:text="Login Successful"
        android:textSize="34sp"
        app:layout_constraintEnd_toEndOf="parent"
        tools:layout_editor_absoluteY="59dp" />
</RelativeLayout>
login successfull JAVA
package com.example.loginapplication;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

public class LoginSuccesful extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login_succesful);
    }
}
"""

def p4():
    return """<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="CHANGING WALLPAPER APPLICATION"
        android:textColor="@color/black"
        android:textStyle="bold"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.496"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.063" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginStart="72dp"
        android:layout_marginTop="53dp"
        android:layout_marginEnd="35dp"
        android:layout_marginBottom="590dp"
        android:text="CLICK HERE TO CHANGE WALLPAPER"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.820"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.0" />

</RelativeLayout>
Java
package com.example.changingwalpaper;

import androidx.appcompat.app.AppCompatActivity;
import android.app.WallpaperManager;
import android.graphics.Bitmap;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import java.io.IOException;
import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity {

    Button changewallpaper;
    Timer mytimer;
    Drawable drawable;
    WallpaperManager wpm;
    int prev = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mytimer = new Timer();
        wpm = WallpaperManager.getInstance(this);

        changewallpaper = findViewById(R.id.button);
        changewallpaper.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                setWallpaper();
            }
        });
    }

    private void setWallpaper() {
        mytimer.schedule(new TimerTask() {
            @Override
            public void run() {
                if (prev == 1) {
                    drawable = getResources().getDrawable(R.drawable.one);
                    prev = 2;
                } else if (prev == 2) {
                    drawable = getResources().getDrawable(R.drawable.two);
                    prev = 3;
                }

                Bitmap wallpaper = ((BitmapDrawable) drawable).getBitmap();
                try {
                    wpm.setBitmap(wallpaper);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }, 0, 30000);
    }
}
"""

def p5():
    return """<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="378dp"
        android:layout_height="68dp"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="18dp"
        android:layout_marginBottom="602dp"
        android:text="Counter Application"
        android:textSize="38dp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <TextView
        android:id="@+id/textView"
        android:layout_width="121dp"
        android:layout_height="32dp"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="145dp"
        android:layout_marginBottom="478dp"
        android:text="Counter Value" />

    <Button
        android:id="@+id/btn_start"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="297dp"
        android:layout_marginBottom="295dp"
        android:text="Start" />

    <Button
        android:id="@+id/btn_stop"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="74dp"
        android:layout_marginBottom="292dp"
        android:text="Stop" />

</RelativeLayout>
JAVA
package com.example.counter;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    Button btnstart, btnstop;
    TextView txtcounter;
    int i = 1;
    Handler customHandler = new Handler();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnstart = findViewById(R.id.btn_start);
        btnstop = findViewById(R.id.btn_stop);
        txtcounter = findViewById(R.id.textView);

        btnstart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                customHandler.postDelayed(updateTimerThread, 0);
            }
        });

        btnstop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                customHandler.removeCallbacks(updateTimerThread);
            }
        });
    }

    private final Runnable updateTimerThread = new Runnable() {
        @Override
        public void run() {
            txtcounter.setText("" + i);
            customHandler.postDelayed(this, 1000);
            i++;
        }
    };
}
"""

def p6():
    return """<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentRight="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="59dp"
        android:layout_marginRight="59dp"
        android:layout_marginBottom="649dp"
        android:text="Text2SpeechApp"
        android:textSize="40dp" />

    <EditText
        android:id="@+id/editText"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentRight="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="101dp"
        android:layout_marginRight="101dp"
        android:layout_marginBottom="514dp"
        android:ems="10"
        android:hint="Enter the text to be converted"
        android:inputType="textPersonName"
        android:text="" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentRight="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="162dp"
        android:onClick="convert"
        android:layout_marginRight="162dp"
        android:layout_marginBottom="329dp"
        android:text="Convert" />

</RelativeLayout>
JAVA
package com.example.texttospeech;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    TextToSpeech t1;
    EditText e1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        e1 = findViewById(R.id.editText);

        t1 = new TextToSpeech(getApplicationContext(), new
                TextToSpeech.OnInitListener() {
                    @Override
                    public void onInit(int status) {
                        if (status != TextToSpeech.ERROR) {
                            t1.setLanguage(Locale.UK);
                        }
                    }
                });
    }

    public void convert(View view) {
        String tospeak = e1.getText().toString();
        t1.speak(tospeak, TextToSpeech.QUEUE_FLUSH, null);
    }
}
"""

def p7():
    return """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <!-- ... (Other Views) ... -->

    <TableLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="32dp"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@id/phoneNumberEditText">

        <!-- ... (Other Rows and Buttons) ... -->

        <TableRow
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:gravity="center_horizontal">

            <Button
                android:id="@+id/callBtn"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_margin="8dp"
                android:text="Call" />

            <Button
                android:id="@+id/saveBtn"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_margin="8dp"
                android:text="Save" />
        </TableRow>
    </TableLayout>

</androidx.constraintlayout.widget.ConstraintLayout>
JAVA
package com.example.call;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    EditText phoneNumberEditText;
    Button clearBtn, callBtn, saveBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        phoneNumberEditText = findViewById(R.id.phoneNumberEditText);
        clearBtn = findViewById(R.id.clearBtn);
        callBtn = findViewById(R.id.callBtn);
        saveBtn = findViewById(R.id.saveBtn);

        clearBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                phoneNumberEditText.setText("");
            }
        });

        callBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String phoneNumber = phoneNumberEditText.getText().toString();
                Intent intent = new Intent(Intent.ACTION_DIAL);
                intent.setData(Uri.parse("tel:" + phoneNumber));
                startActivity(intent);
            }
        });

        saveBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String phoneNumber = phoneNumberEditText.getText().toString();
                Intent intent = new Intent(Intent.ACTION_INSERT);
                intent.setType(ContactsContract.Contacts.CONTENT_TYPE);
                intent.putExtra(ContactsContract.Intents.Insert.PHONE, phoneNumber);
                startActivity(intent);
            }
        });
    }

    public void inputNumber(View v) {
        Button btn = (Button)v;
        String digit = btn.getText().toString();
        String phoneNumber = phoneNumberEditText.getText().toString();
        phoneNumberEditText.setText(phoneNumber + digit);
    }
}
"""