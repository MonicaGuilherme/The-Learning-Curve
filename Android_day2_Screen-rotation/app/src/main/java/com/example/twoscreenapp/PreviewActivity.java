package com.example.twoscreenapp;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class PreviewActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
                setContentView(R.layout.activity_preview);

                Intent intent = getIntent();
                String namePreview = intent.getStringExtra(MainActivity.NAME_TEXT);
                String bioPreview = intent.getStringExtra(MainActivity.BIO_TEXT);

        TextView copyName = findViewById(R.id.nameView);
        copyName.setText(namePreview.isEmpty() ? "No input, please right your name" : namePreview);

        TextView copyBio = findViewById(R.id.bioView);
        copyBio.setText(bioPreview.isEmpty() ? "No information to show" : bioPreview);

        Button backButton = findViewById(R.id.button_back);
        backButton.setOnClickListener(v -> finish());
        };
    }
