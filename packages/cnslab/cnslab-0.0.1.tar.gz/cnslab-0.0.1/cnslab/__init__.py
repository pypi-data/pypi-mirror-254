def p1():
    return """#include <stdio.h>
#include <stdlib.h>

main() {
    int key;
    char ip[100], op[100];
    
    printf("Enter the word: ");
    gets(ip);
    printf("Enter the key: ");
    scanf("%d", &key);
    
    for (int i = 0; i < strlen(ip); i++) {
        op[i] = ip[i] + key;
        if (op[i] > 122) {
            op[i] = op[i] - 122 + 96;
        }
    }
    
    printf("output: %s", op);
}
"""

def p2():
    return """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 30

void toLowerCase(char plain[], int ps)
{
    int i;
    for (i = 0; i < ps; i++) {
        if (plain[i] > 64 && plain[i] < 91)
            plain[i] += 32;
    }
}

int removeSpaces(char* plain, int ps)
{
    int i, count = 0;
    for (i = 0; i < ps; i++)
        if (plain[i] != ' ')
            plain[count++] = plain[i];
    plain[count] = '\0';
    return count;
}

void generateKeyTable(char key[], int ks, char keyT[5][5])
{
    int i, j, k, flag = 0, *dicty;

    dicty = (int*)calloc(26, sizeof(int));
    for (i = 0; i < ks; i++) {
        if (key[i] != 'j')
            dicty[key[i] - 97] = 2;
    }
    dicty['j' - 97] = 1;
    i = 0;
    j = 0;
    for (k = 0; k < ks; k++) {
        if (dicty[key[k] - 97] == 2) {
            dicty[key[k] - 97] -= 1;
            keyT[i][j] = key[k];
            j++;
            if (j == 5) {
                i++;
                j = 0;
            }
        }
    }
    for (k = 0; k < 26; k++) {
        if (dicty[k] == 0) {
            keyT[i][j] = (char)(k + 97);
            j++;
            if (j == 5) {
                i++;
                j = 0;
            }
        }
    }
}

void search(char keyT[5][5], char a, char b, int arr[])
{
    int i, j;
    if (a == 'j')
        a = 'i';
    else if (b == 'j')
        b = 'i';
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 5; j++) {
            if (keyT[i][j] == a) {
                arr[0] = i;
                arr[1] = j;
            }
            else if (keyT[i][j] == b) {
                arr[2] = i;
                arr[3] = j;
            }
        }
    }
}

int mod5(int a)
{
    return (a % 5);
}

int prepare(char str[], int ptrs)
{
    if (ptrs % 2 != 0) {
        str[ptrs++] = 'z';
        str[ptrs] = '\0';
    }
    return ptrs;
}

void encrypt(char str[], char keyT[5][5], int ps)
{
    int i, a[4];
    for (i = 0; i < ps; i += 2) {
        search(keyT, str[i], str[i + 1], a);
        if (a[0] == a[2]) {
            str[i] = keyT[a[0]][mod5(a[1] + 1)];
            str[i + 1] = keyT[a[0]][mod5(a[3] + 1)];
        }
        else if (a[1] == a[3]) {
            str[i] = keyT[mod5(a[0] + 1)][a[1]];
            str[i + 1] = keyT[mod5(a[2] + 1)][a[1]];
        }
        else {
            str[i] = keyT[a[0]][a[3]];
            str[i + 1] = keyT[a[2]][a[1]];
        }
    }
}

void encryptByPlayfairCipher(char str[], char key[])
{
    char ps, ks, keyT[5][5];

    ks = strlen(key);
    ks = removeSpaces(key, ks);
    toLowerCase(key, ks);

    ps = strlen(str);
    toLowerCase(str, ps);
    ps = removeSpaces(str, ps);
    ps = prepare(str, ps);
    generateKeyTable(key, ks, keyT);
    encrypt(str, keyT, ps);
}

int main()
{
    char str[SIZE], key[SIZE];

    strcpy(key, "Monarchy");
    printf("Key text: %s\n", key);

    strcpy(str, "instruments");
    printf("Plain text: %s\n", str);

    encryptByPlayfairCipher(str, key);
    printf("Cipher text: %s\n", str);
    return 0;
}
"""

def p3():
    return """
#include<stdio.h>
#include<string.h>

int main() {
    unsigned int a[3][3] = { { 6, 24, 1 }, { 13, 16, 10 }, { 20, 17, 15 } };
    unsigned int b[3][3] = { { 8, 5, 10 }, { 21, 8, 21 }, { 21, 12, 8 } };
    int i, j;
    unsigned int c[20], d[20];
    char msg[20];
    int determinant = 0, t = 0;
    
    printf("Enter plain text\n ");
    scanf("%s", msg);
    
    for (i = 0; i < 3; i++) {
        c[i] = msg[i] - 65;
        printf("%d ", c[i]);
    }
    
    for (i = 0; i < 3; i++) {
        t = 0;
        for (j = 0; j < 3; j++) {
            t = t + (a[i][j] * c[j]);
        }
        d[i] = t % 26;
    }
    
    printf("\nEncrypted Cipher Text :");
    for (i = 0; i < 3; i++)
        printf(" %c", d[i] + 65);
    
    for (i = 0; i < 3; i++) {
        t = 0;
        for (j = 0; j < 3; j++) {
            t = t + (b[i][j] * d[j]);
        }
        c[i] = t % 26;
    }
    
    printf("\nDecrypted Cipher Text :");
    for (i = 0; i < 3; i++)
        printf(" %c", c[i] + 65);
    
    return 0;
}
"""

def p4():
    return """
#include<stdio.h>
#include<string.h>

int main(){
    char msg[] = "THECRAZYPROGRAMMER";
    char key[] = "HELLO";
    int msgLen = strlen(msg), keyLen = strlen(key), i, j;
    char newKey[msgLen], encryptedMsg[msgLen], decryptedMsg[msgLen];
    
    // Generating new key
    for(i = 0, j = 0; i < msgLen; ++i, ++j){
        if(j == keyLen)
            j = 0;
        newKey[i] = key[j];
    }
    newKey[i] = '\0';
    
    // Encryption
    for(i = 0; i < msgLen; ++i)
        encryptedMsg[i] = ((msg[i] + newKey[i]) % 26) + 'A';
    encryptedMsg[i] = '\0';
    
    // Decryption
    for(i = 0; i < msgLen; ++i)
        decryptedMsg[i] = (((encryptedMsg[i] - newKey[i]) + 26) % 26) + 'A';
    decryptedMsg[i] = '\0';
    
    printf("Original Message: %s", msg);
    printf("\nKey: %s", key);
    printf("\nNew Generated Key: %s", newKey);
    printf("\nEncrypted Message: %s", encryptedMsg);
    printf("\nDecrypted Message: %s", decryptedMsg);
    
    return 0;
}
"""

def p5():
    return """
#include <stdio.h>
#include <string.h>

int main() {
    int i, j, len, rails, count, code[100][1000];
    char str[1000];

    printf("Enter a Secret Message:\n");
    fgets(str, sizeof(str), stdin);
    len = strlen(str);

    // Remove the newline character from the input string
    if (len > 0 && str[len - 1] == '\n') {
        str[--len] = '\0';
    }

    printf("Enter the number of rails:\n");
    scanf("%d", &rails);

    if (rails <= 0) {
        printf("Number of rails should be a positive integer.\n");
        return 1;
    }

    for (i = 0; i < rails; i++) {
        for (j = 0; j < len; j++) {
            code[i][j] = 0;
        }
    }

    count = 0;
    j = 0;

    while (j < len) {
        if (count % 2 == 0) {
            for (i = 0; i < rails; i++) {
                code[i][j] = (int)str[j];
                j++;
            }
        } else {
            for (i = rails - 2; i > 0; i--) {
                code[i][j] = (int)str[j];
                j++;
            }
        }
        count++;
    }

    printf("Encrypted Message: ");
    for (i = 0; i < rails; i++) {
        for (j = 0; j < len; j++) {
            if (code[i][j] != 0) {
                printf("%c", (char)code[i][j]);
            }
        }
    }
    printf("\n");

    return 0;
}
"""

def p6():
    return """
//DES algorihm 
//filename should be as class name : DES.java
import javax.swing.*;
import java.security.SecureRandom;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.util.Random ;
class DES {
byte[] skey = new byte[1000];
String skeyString;
static byte[] raw;
String inputMessage,encryptedData,decryptedMessage;

public DES() {
try {
generateSymmetricKey();

inputMessage=JOptionPane.showInputDialog(null,"Enter message to encrypt");
byte[] ibyte = inputMessage.getBytes();
byte[] ebyte=encrypt(raw, ibyte);
String encryptedData = new String(ebyte);
System.out.println("Encrypted message "+encryptedData);
JOptionPane.showMessageDialog(null,"Encrypted Data "+"\n"+encryptedData);

byte[] dbyte= decrypt(raw,ebyte);
String decryptedMessage = new String(dbyte);
System.out.println("Decrypted message "+decryptedMessage);

JOptionPane.showMessageDialog(null,"Decrypted Data "+"\n"+decryptedMessage);
}
catch(Exception e) {
System.out.println(e);
}

}
void generateSymmetricKey() {
try {
Random r = new Random();
int num = r.nextInt(10000);
String knum = String.valueOf(num);
byte[] knumb = knum.getBytes();
skey=getRawKey(knumb);
skeyString = new String(skey);
System.out.println("DES Symmetric key = "+skeyString);
}
catch(Exception e) {
System.out.println(e);
}
}
private static byte[] getRawKey(byte[] seed) throws Exception {
KeyGenerator kgen = KeyGenerator.getInstance("DES");
SecureRandom sr = SecureRandom.getInstance("SHA1PRNG");
sr.setSeed(seed);
kgen.init(56, sr);
SecretKey skey = kgen.generateKey();
raw = skey.getEncoded();
return raw;
}
private static byte[] encrypt(byte[] raw, byte[] clear) throws Exception {
SecretKeySpec skeySpec = new SecretKeySpec(raw, "DES");
Cipher cipher = Cipher.getInstance("DES");
cipher.init(Cipher.ENCRYPT_MODE, skeySpec);
byte[] encrypted = cipher.doFinal(clear);
return encrypted;
}

private static byte[] decrypt(byte[] raw, byte[] encrypted) throws Exception {
SecretKeySpec skeySpec = new SecretKeySpec(raw, "DES");
Cipher cipher = Cipher.getInstance("DES");
cipher.init(Cipher.DECRYPT_MODE, skeySpec);
byte[] decrypted = cipher.doFinal(encrypted);
return decrypted;
}
public static void main(String args[]) {
DES des = new DES();
}
}
"""

def p7():
    return """

// Java program to calculate SHA-1 hash value

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class GFG {
	public static String encryptThisString(String input)
	{
		try {
			// getInstance() method is called with algorithm SHA-1
			MessageDigest md = MessageDigest.getInstance("SHA-1");

			// digest() method is called
			// to calculate message digest of the input string
			// returned as array of byte
			byte[] messageDigest = md.digest(input.getBytes());

			// Convert byte array into signum representation
			BigInteger no = new BigInteger(1, messageDigest);

			// Convert message digest into hex value
			String hashtext = no.toString(16);

			// Add preceding 0s to make it 32 bit
			while (hashtext.length() < 32) {
				hashtext = "0" + hashtext;
			}

			// return the HashText
			return hashtext;
		}

		// For specifying wrong message digest algorithms
		catch (NoSuchAlgorithmException e) {
			throw new RuntimeException(e);
		}
	}

	// Driver code
	public static void main(String args[]) throws
									NoSuchAlgorithmException
	{

		System.out.println("HashCode Generated by SHA-1 for: ");

		String s1 = "GeeksForGeeks";
		System.out.println("\n" + s1 + " : " + encryptThisString(s1));

		String s2 = "hello world";
		System.out.println("\n" + s2 + " : " + encryptThisString(s2));
	}
}
"""

def p8():
    return """ 
//md5
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

// Java program to calculate MD5 hash value
public class MD5 {
	public static String getMd5(String input)
	{
		try {

			// Static getInstance method is called with hashing MD5
			MessageDigest md = MessageDigest.getInstance("MD5");

		
			byte[] messageDigest = md.digest(input.getBytes());

	
			BigInteger no = new BigInteger(1, messageDigest);

			String hashtext = no.toString(16);
			while (hashtext.length() < 32) {
				hashtext = "0" + hashtext;
			}
			return hashtext;
		}

	
		catch (NoSuchAlgorithmException e) {
			throw new RuntimeException(e);
		}
	}

	public static void main(String args[]) throws NoSuchAlgorithmException
	{
		String s = "GeeksForGeeks";
		System.out.println("Your HashCode Generated by MD5 is: " + getMd5(s));
	}
}
"""
def p9():
    return """ 
import java.security.*;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;

public class DigitalSignature {

    public static void main(String[] args) {
        try {
            // Generate key pair
            KeyPair keyPair = generateKeyPair();

            // Get private and public keys
            PrivateKey privateKey = keyPair.getPrivate();
            PublicKey publicKey = keyPair.getPublic();

            // Create a sample message
            String message = "Hello, Digital Signature!";

            // Sign the message
            byte[] signature = signMessage(message, privateKey);

            // Verify the signature
            boolean isVerified = verifySignature(message, signature, publicKey);

            System.out.println("Original Message: " + message);
            System.out.println("Signature: " + Base64.getEncoder().encodeToString(signature));
            System.out.println("Signature Verified: " + isVerified);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Generate DSS key pair
    private static KeyPair generateKeyPair() throws NoSuchAlgorithmException {
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("DSA");
        keyPairGenerator.initialize(2048); // You can adjust the key size as needed
        return keyPairGenerator.generateKeyPair();
    }

    // Sign the message using the private key
    private static byte[] signMessage(String message, PrivateKey privateKey) throws Exception {
        Signature signature = Signature.getInstance("SHA256withDSA");
        signature.initSign(privateKey);
        signature.update(message.getBytes());
        return signature.sign();
    }

    // Verify the signature using the public key
    private static boolean verifySignature(String message, byte[] signature, PublicKey publicKey) throws Exception {
        Signature verifier = Signature.getInstance("SHA256withDSA");
        verifier.initVerify(publicKey);
        verifier.update(message.getBytes());
        return verifier.verify(signature);
    }
}
"""
def p10():
    return """ //fermats
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
    long long int n, res;

    printf("Enter the number: ");
    scanf("%lld", &n);

    for (int a = 2; a < n - 1; a++) {
        res = (long long int)pow(a, n - 1) % n;
        if (res != 1) {
            printf("The number is not prime\n");
            exit(0);
        }
    }
    printf("The number is prime\n");

    return 0;
}


//eulers
#include <stdio.h>

int gcd(int a, int b) {
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

int phi(unsigned int n) {
    unsigned int result = 1;
    for (int i = 2; i < n; i++)
        if (gcd(i, n) == 1)
            result++;
    return result;
}

int main() {
    int n;
    for (n = 1; n <= 10; n++)
        printf("phi(%d) = %d\n", n, phi(n));
    return 0;
}
"""
def p11():
    return """ 
import java.io.*;
import java.math.*;
import java.util.*;

public class GFG {
    public static double gcd(double a, double h) {
        double temp;
        while (true) {
            temp = a % h;
            if (temp == 0)
                return h;
            a = h;
            h = temp;
        }
    }

    public static void main(String[] args) {
        double p = 3;
        double q = 7;

        double n = p * q;

        // double e stands for encrypt
        double e = 2;
        double phi = (p - 1) * (q - 1);
        while (e < phi) {

            if (gcd(e, phi) == 1)
                break;
            else
                e++;
        }
        int k = 2;
        double d = (1 + (k * phi)) / e;

        // Message to be encrypted
        double msg = 12;

        System.out.println("Message data = " + msg);

        // Encryption c = (msg ^ e) % n
        double c = Math.pow(msg, e);
        c = c % n;
        System.out.println("Encrypted data = " + c);

        // Decryption m = (c ^ d) % n
        double m = Math.pow(c, d);
        m = m % n;
        System.out.println("Original Message Sent = " + m);
    }
}
"""
def p12():
    return """ 
#include <math.h>
#include <stdio.h>

long long int power(long long int a, long long int b,
                    long long int P)
{
    if (b == 1)
        return a;
    else
        return (((long long int)pow(a, b)) % P);
}

int main()
{
    long long int P, G, x, a, y, b, ka, kb;

    P = 23;
    printf("The value of P: %lld\n", P);

    G = 9;
    printf("The value of G: %lld\n\n", G);

    a = 4;
    printf("The private key a for Alice: %lld\n", a);
    x = power(G, a, P);

    b = 3;
    printf("The private key b for Bob: %lld\n\n", b);
    y = power(G, b, P);

    ka = power(y, a, P);
    kb = power(x, b, P);

    printf("Secret key for Alice is: %lld\n", ka);
    printf("Secret Key for Bob is: %lld\n", kb);

    return 0;
}
"""
def p13():
    return """ 
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.util.Base64;

public class AESExample {

    public static void main(String[] args) throws Exception {
        SecretKey key = KeyGenerator.getInstance("AES").generateKey();
        String message = "Hello, AES encryption!";
        String encryptedText = encrypt(message, key);
        System.out.println("Encrypted: " + encryptedText);
        System.out.println("Decrypted: " + decrypt(encryptedText, key));
    }

    private static String encrypt(String text, SecretKey key) throws Exception {
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, key);
        return Base64.getEncoder().encodeToString(cipher.doFinal(text.getBytes()));
    }

    private static String decrypt(String text, SecretKey key) throws Exception {
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.DECRYPT_MODE, key);
        return new String(cipher.doFinal(Base64.getDecoder().decode(text)));
    }
}
"""