package com.example.twoscreenapp;

import android.content.Intent;
import android.os.Bundle;
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
                //String bioPreview = intent.getStringExtra(MainActivity.)

        TextView copyName = findViewById(R.id.nameView);
        copyName.setText(namePreview);

        };
    }
