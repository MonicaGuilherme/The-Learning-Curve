package com.training.usermanager;

import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class AddUserActivity extends AppCompatActivity {

    private EditText editTextName, editTextAge, editTextEmail, editTextAvatar;
    private UserDatabaseHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_user);

        dbHelper = new UserDatabaseHelper(this);

        editTextName = findViewById(R.id.editTextName);
        editTextAge = findViewById(R.id.editTextAge);
        editTextEmail = findViewById(R.id.editTextEmail);
        editTextAvatar = findViewById(R.id.editTextAvatar);

        Button buttonSave = findViewById(R.id.buttonSave);
        Button buttonReset = findViewById(R.id.buttonReset);

        buttonSave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                saveUser();
            }
        });

        buttonReset.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                resetForm();
            }
        });
    }

    private void saveUser() {
        String name = editTextName.getText().toString().trim();
        String ageStr = editTextAge.getText().toString().trim();
        String email = editTextEmail.getText().toString().trim();
        String avatar = editTextAvatar.getText().toString().trim();

        if (TextUtils.isEmpty(name)) {
            editTextName.setError("Name is required");
            return;
        }

        if (TextUtils.isEmpty(ageStr)) {
            editTextAge.setError("Age is required");
            return;
        }

        int age;
        try {
            age = Integer.parseInt(ageStr);
        } catch (NumberFormatException e) {
            editTextAge.setError("Age must be a number");
            return;
        }

        if (TextUtils.isEmpty(email)) {
            editTextEmail.setError("Email is required");
            return;
        }

        // Avatar URL is optional

        User user = new User(0, name, age, email, avatar);
        dbHelper.addUser(user);
        Toast.makeText(this, "User added successfully!", Toast.LENGTH_SHORT).show();
        finish(); // go back to MainActivity
    }

    private void resetForm() {
        editTextName.setText("");
        editTextAge.setText("");
        editTextEmail.setText("");
        editTextAvatar.setText("");
    }
}

