package com.example.twoscreenapp;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    public final static String NAME_TEXT = "name_text";
    public final static String BIO_TEXT = "bio_text";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText name = findViewById(R.id.text_name);
        EditText bio = findViewById(R.id.text_bio);

        Button previewBtn = findViewById((R.id.button_preview));
        Button linkedinButton = findViewById(R.id.button_linkedIn);

        previewBtn.setOnClickListener(v -> {
            String nameText = name.getText().toString();
            String bioText = bio.getText().toString();

            Intent intent = new Intent(this, PreviewActivity.class);
            intent.putExtra(NAME_TEXT,nameText);
            intent.putExtra(BIO_TEXT, bioText);

            startActivity(intent);
        });

        linkedinButton.setOnClickListener(v ->  {
                String url = "https://www.linkedin.com/in/monica-guilherme";
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                startActivity(intent);
        });
    }
}