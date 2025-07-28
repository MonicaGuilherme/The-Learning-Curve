package com.training.helloworld;

import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button btn = findViewById(R.id.button);
        TextView textView = findViewById(R.id.textView);
        EditText editText = findViewById(R.id.editText);

        btn.setOnClickListener(v -> {
            Log.d("xpto","Button callback executing");

            textView.setText(R.string.textview);
            editText.setText("");

        });


        editText.setOnEditorActionListener((v, actionId, e) -> {

            Log.d("XPTO","Edit Text callback executing...");

            CharSequence text = v.getText();
            if(!text.toString().isEmpty()){
                textView.setText(v.getText());
                v.setText("");
            }


            return true;
        });

    }
}