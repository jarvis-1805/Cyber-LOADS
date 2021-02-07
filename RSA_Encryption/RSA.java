import java.math.BigInteger;
import java.security.SecureRandom;

class RSAalgorithm
{
	//this is the e after calculations
	private BigInteger publicKey;
	
	//this is the d parameter after the calculations
	private BigInteger privateKey;
	
	//this is n=p*q
	private BigInteger n;
	
	//we need random number generator
	private SecureRandom random;
	
	public RSAalgorithm()
	{
		this.random = new SecureRandom();
	}
	
	public BigInteger encryptMessage(String message)
	{
		return encrypt(this.publicKey, this.n, message);
	}
	
	public String decryptMessage(BigInteger cipherText)
	{
		return decrypt(this.privateKey, this.n, cipherText);
	}
	
	private String decrypt(BigInteger d, BigInteger n, BigInteger cipherText)
	{
		//we use modular exponentiation in decryption as well: cipher^d mod n
		BigInteger messageInt = cipherText.modPow(d, n);
		
		//we want to end with a String
		return new String(messageInt.toByteArray());
	}
	
	//the cipher text will be a huge integer
	private BigInteger encrypt(BigInteger e, BigInteger n, String message)
	{
		//first we transforms the original message into an array of bytes
		byte[] messageBytes = message.getBytes();
		
		BigInteger messageInt = new BigInteger(messageBytes);
		
		//we have to use modular exponentiation message^e mod n is the cipher text
		return messageInt.modPow(e, n);
	}
	
	public void generateKeys(int keyDigits)
	{
		//p is large prime number
		BigInteger p = BigInteger.probablePrime(keyDigits, random);
		
		//q is a large prime number
		BigInteger q = BigInteger.probablePrime(keyDigits, random);
		
		//n=p*q this is the trap-door function
		this.n = p.multiply(q);
		
		//Euler's totient phi function
		BigInteger phi = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));
		
		//e<phi is comprime to phi so gcd(e, phi) = 1
		BigInteger e = generatePublicFactor(phi);
		
		//d is the modular inverse of e (with mod phi)
		BigInteger d = e.modInverse(phi);
		
		this.privateKey = d;
		this.publicKey = e;
	}
	
	//this is how we calculate the e parameter
	private BigInteger generatePublicFactor(BigInteger phi)
	{
		BigInteger e = new BigInteger(phi.bitLength(), this.random);
		
		//we are after a coprime where gcd(e, phi) = 1 so let iterate
		while(!e.gcd(phi).equals(BigInteger.ONE))
			e = new BigInteger(phi.bitLength(), this.random);
		
		return e;
	}
}

public class RSA
{
	public static void main(String args[])
	{
		RSAalgorithm rsa = new RSAalgorithm();
		rsa.generateKeys(1024);
		
		String originalMessage = "Hey! This is a secrete message encrypted with RSA!";
		System.out.println("Encrypted message by Alice: " + originalMessage);
		BigInteger cipher = rsa.encryptMessage(originalMessage);
		System.out.println("Cipher text: " + cipher);
		System.out.println("Decrypted message by Bob: " + rsa.decryptMessage(cipher));
	}
}