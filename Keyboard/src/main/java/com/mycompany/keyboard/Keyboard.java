package com.mycompany.keyboard;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 *
 * @author alexa
 */
public class Keyboard {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Keyboard Recommendation System");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        JPanel panel = new JPanel();
        frame.add(panel);
        placeComponents(panel);

        frame.setVisible(true);
    }

    private static void placeComponents(JPanel panel) {
        panel.setLayout(null);

        JLabel preferenceLabel = new JLabel("Enter Preference:");
        preferenceLabel.setBounds(10, 20, 160, 25);
        panel.add(preferenceLabel);

        JTextField preferenceText = new JTextField(20);
        preferenceText.setBounds(180, 20, 165, 25);
        panel.add(preferenceText);

        JButton recommendButton = new JButton("Recommend");
        recommendButton.setBounds(10, 80, 160, 25);
        panel.add(recommendButton);

        JTextArea resultArea = new JTextArea();
        resultArea.setBounds(10, 120, 335, 120);
        panel.add(resultArea);

        recommendButton.addActionListener((ActionEvent e) -> {
            String preference = preferenceText.getText();
            try {
                String result = runPythonScript(preference);
                resultArea.setText(result);
            } catch (Exception ex) {
                resultArea.setText("Error: " + ex.getMessage());
            }
        });
    }

    private static String runPythonScript(String preference) throws Exception {
        String pythonScriptPath = "path/to/your/Keyboard.py";
        ProcessBuilder pb = new ProcessBuilder("python", pythonScriptPath, preference);
        pb.redirectErrorStream(true);
        Process process = pb.start();
        
        StringBuilder result;
        try (BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
            String line;
            result = new StringBuilder();
            while ((line = in.readLine()) != null) {
                result.append(line).append("\n");
            }
        }
        return result.toString();
    }
}
