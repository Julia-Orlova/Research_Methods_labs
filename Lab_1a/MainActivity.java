package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private TextView showFactors;
    private EditText nEdit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        nEdit = (EditText) findViewById(R.id.input);
        showFactors = (TextView) findViewById(R.id.output);

    }

    public void FermatFactors(View view)
    {
        try {
            long time_begin = System.currentTimeMillis();
            int n = Integer.parseInt(nEdit.getText().toString());
            // Перевірка на необхідну додатність числа
            if (n <= 0) {
                Toast exc1 = Toast.makeText(this, "Введене число недодатнє, факторизація методом Ферма неможлива", Toast.LENGTH_SHORT);
                exc1.show();
                return;
            }

            int a = (int) Math.ceil(Math.sqrt(n));

            // Перевірка чи n не є квадратним числом
            if (a * a == n) {
                String res = "Число є квадратом!\n" + a + " * " + a + " = " + n;
                showFactors.setText(res);
                return;
            }

            // Перевірка на парність числа
            if ((n % 2) == 0) {
                String res = "Число парне!\n" + n/2 + " * " + 2 + " = " + n;
                showFactors.setText(res);
                return;
            }

            int b;
            while (true) {
                int b1 = a * a - n;
                b = (int) (Math.sqrt(b1));

                if (b * b == b1)
                    break;
                else
                    a += 1;
            }

            String res = "Результат:\na = " + a + "\nb = " + b + "\n(a - b)(a + b) = " + (a - b) + " * " + (a + b) + " = " + n;
            showFactors.setText(res);


        } catch (Exception e) {
            Toast exc2 = Toast.makeText(this, "Некоректний ввід", Toast.LENGTH_SHORT);
            exc2.show();
        }
    }
}
