package com.example.financetracker.ui.screens

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.financetracker.data.CreditCard
import com.example.financetracker.ui.theme.*

@Composable
fun CardsScreen(navController: NavController) {
    var cards by remember { mutableStateOf(listOf<CreditCard>()) }
    var showAddDialog by remember { mutableStateOf(false) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Credit Cards") },
                navigationIcon = {
                    IconButton(onClick = { navController.navigateUp() }) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back")
                    }
                },
                actions = {
                    IconButton(onClick = { showAddDialog = true }) {
                        Icon(Icons.Default.Add, contentDescription = "Add Card")
                    }
                }
            )
        }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
        ) {
            // Total Cards Balance
            Card(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp),
                colors = CardDefaults.cardColors(containerColor = CardBackground)
            ) {
                Column(
                    modifier = Modifier.padding(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(
                        text = "Total Cards Balance",
                        style = MaterialTheme.typography.titleLarge,
                        color = TextSecondary
                    )
                    Text(
                        text = "$${cards.sumOf { it.balance }.format(2)}",
                        style = MaterialTheme.typography.displayLarge,
                        color = TextPrimary
                    )
                }
            }

            // Cards List
            LazyColumn(
                modifier = Modifier.fillMaxSize(),
                contentPadding = PaddingValues(16.dp),
                verticalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                items(cards) { card ->
                    CardItem(card = card)
                }
            }
        }

        if (showAddDialog) {
            AddCardDialog(
                onDismiss = { showAddDialog = false },
                onAdd = { /* TODO: Implement add card */ }
            )
        }
    }
}

@Composable
fun CardItem(card: CreditCard) {
    Card(
        modifier = Modifier.fillMaxWidth(),
        colors = CardDefaults.cardColors(containerColor = CardBackground)
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp)
        ) {
            // Card Header
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = "•••• ${card.cardNumber.takeLast(4)}",
                    style = MaterialTheme.typography.titleLarge
                )
                IconButton(onClick = { /* TODO: Implement delete card */ }) {
                    Icon(Icons.Default.Delete, contentDescription = "Delete Card")
                }
            }

            // Card Details
            Spacer(modifier = Modifier.height(8.dp))
            Text(
                text = card.cardHolder,
                style = MaterialTheme.typography.bodyLarge,
                color = TextSecondary
            )
            Text(
                text = "Expires: ${card.expiryDate}",
                style = MaterialTheme.typography.bodyLarge,
                color = TextSecondary
            )

            // Balance
            Spacer(modifier = Modifier.height(8.dp))
            Text(
                text = "Balance: $${card.balance.format(2)}",
                style = MaterialTheme.typography.titleLarge,
                color = TextPrimary
            )
        }
    }
}

@Composable
fun AddCardDialog(
    onDismiss: () -> Unit,
    onAdd: (CreditCard) -> Unit
) {
    var cardNumber by remember { mutableStateOf("") }
    var cardHolder by remember { mutableStateOf("") }
    var expiryDate by remember { mutableStateOf("") }
    var balance by remember { mutableStateOf("") }

    AlertDialog(
        onDismissRequest = onDismiss,
        title = { Text("Add Credit Card") },
        text = {
            Column(
                modifier = Modifier.fillMaxWidth(),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                // Card Number
                OutlinedTextField(
                    value = cardNumber,
                    onValueChange = { cardNumber = it },
                    label = { Text("Card Number") },
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number)
                )

                // Card Holder
                OutlinedTextField(
                    value = cardHolder,
                    onValueChange = { cardHolder = it },
                    label = { Text("Card Holder") }
                )

                // Expiry Date
                OutlinedTextField(
                    value = expiryDate,
                    onValueChange = { expiryDate = it },
                    label = { Text("Expiry Date (MM/YY)") }
                )

                // Initial Balance
                OutlinedTextField(
                    value = balance,
                    onValueChange = { balance = it },
                    label = { Text("Initial Balance") },
                    prefix = { Text("$") },
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number)
                )
            }
        },
        confirmButton = {
            TextButton(
                onClick = {
                    val newCard = CreditCard(
                        cardNumber = cardNumber,
                        cardHolder = cardHolder,
                        expiryDate = expiryDate,
                        balance = balance.toDoubleOrNull() ?: 0.0
                    )
                    onAdd(newCard)
                    onDismiss()
                }
            ) {
                Text("Add")
            }
        },
        dismissButton = {
            TextButton(onClick = onDismiss) {
                Text("Cancel")
            }
        }
    )
} 