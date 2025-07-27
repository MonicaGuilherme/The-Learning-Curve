package com.example.twoscreenapp;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    public final static String NAME_TEXT = "name_text";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText name = findViewById(R.id.text_name);
        Button previewBtn = findViewById((R.id.button_preview));
        previewBtn.setOnClickListener(v -> {
            String nameText = name.getText().toString();

            Intent intent = new Intent(this, PreviewActivity.class);
            intent.putExtra(NAME_TEXT,nameText);

            startActivity(intent);
        });


    }
}