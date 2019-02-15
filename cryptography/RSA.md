# RSA：现代网络安全的基石

![RSA](https://i.imgur.com/V0WiFoO.png)

## 起源

和 M 讨论RSA，说是RSA是现在网络安全的基石，恰好这学期的老师是 A，然后就想顺便搞明白这个RSA算法。

##  Concepts

* **PKI**: A security architecture that consists of several entities: Certificate Authority (CA), server, client; and covers following techs: public-private key pair, digital certificate, encryption algorithm, hash algorithm, asymmetric/ symmetric encryption
* **Encryption algorithm**: paired with a key to encrypt original message; to decrypt already encrytped message to original message
* **symmetric encryption**: use the same key for encryption/decryption
* **asymmetric encryption**: use public key for encryption; use private key for decryption
* **hash algorithm**: used to convert original message to a fixed length hashed string, which will be used as a unique fingerprint for this particular message. [data integrity]
* **digital certificate**: a certificate like ID, issued by CA, to prove the holder is the real one as it claims
* **CA**: a well-known, trusted entity, issuing digital certificates/ID to web servers, in order to grant trust to them
* **server**: web servers like amazon.com, being visited by consumers via client; also being issued digital certificate by CA
* **client**: web browsers like Chrome, Firefox, make HTTP request to web server as the client for consumers

## II. Why do we need PKI

In many cases, like email transportation, money transaction, we want the sensitive information to be secure, intact; We also want the two entities involved to be authenticated to be the real ones. Thus we have 3 requirements:

* **data security**: encryption algorithm
* **data integrity**: hash algorithm
* **identity authentication**: digital certificate / CA


## Steps to evolve PKI

Senario: A customer using Chrome as client, want to make transaction with web server bank.com. To make sensitive info secure, we evolve our PKI to provide data security, then data integrity, and identity authentication.

## symmetric encryption

client & server use symmetric encryption with a same key to communicate

drawback:

* Hackers can get the shared key when server sends the key to client
* Server cannot safely distribute the shared key to client

## asymmetric encryption (RSA)


RSA algorithm: use public key and private key to encrypt info

* generated at server,
* beginning with 2 large prime numbers, results with 3 prime numbers: n, a, b
* public key: n, a
* private key: n, b
* How to use RSA?
	* original message om, encrypted message em
	* em = om^a % n for encryption using public key: n, a
	* om = em^b % n for decryptin using private key: n, b

Feature:

* only private key can decrypt, public key can only used to encrypt info
* In fact, any one of the two keys can be used to encrypt, but only the other one can decrypt the encrypted message
* private key can also encrypt info, now only public key can decrypt info

Steps:

* client request public key from server
* server response the same public key to anyone who request it
* client encrypt original info with public key, send encrypted message to server. Even though intercepted by hacker, he doesn’t have private key, can’t decrypt
* server receive the encrypted info, use private key to decrypt

Solution to first problem: cannot distribute symmetric key securely

* client & server can use asymmetric encryption to distribute symmetric key
* client request public key from server
* server response the same public key to anyone who request it
* client encrypt symmetric key (symmetric encryption) with public key (asymmetric encryption), send encrypted message to server. Even though intercepted by hacker, he doesn’t have private key, can’t get symmetric key
* server receive the encrypted info (symmetric key), use private key to decrypt
* Now, only client (browser) and server know symmetric key, which can be used to communicate.

## identity authentication

* Problem above: client cannot assert the server is the real server it expect. If the conversation is hacked by hacker when client want to request public key from server, then the sensitive info of client will leak to hacker
* So, before we request public key from server, we first authenticate the server is the real one we expect

How?

* CA is the authority, trusted by browser/server. It signs certificate for server who apply for, by encrypting certificate info (subject+issuer+valid time+public key of subject) with its own private key. Then encrypted info is the signature
* web server has a digital certificate (ID) issued by CA, used for client/browser to check its identity. Server will first send its digital signature to client before sending its public key
* client/browser has a local list of CA and its public key. When request public key from server, it first check the validity of server’s digital certificate, using the public key of the issuer listed on the certificate. If the decrypted info matches, it trust the server. Otherwist, the server is bad!


## data integrity

another problem: even though hackers cannot see the original info, they can still modify encrypted info, sometimes the modified info is still meaningful, but is not what we want

Solution: **fingerprint**

* human kind uses fingerprint to uniquely identify a person, instead of all kinds of features of this person. It is short, and easy to check
* In fact, it is a way to convert massive info to unique short info
* For message, we use hash algorithm to get the fingerprint of that message. 4 features of hash algorithm:

	* fixed length, short
	* avalanche effect: minor different in original message can lead to significant difference in fingerprints
	* no collision: two different messages shouldn’t share same fingerprint
	* uniqueness: two fingerprints shouldn’t be calculted by one message

Steps:

* server hashes message using a hash algorithm, then append the hashed fingerprint and hash algorithm. It then encryptes the 3 items using private key, and sends to clients
* clients receive message from server, decrypt message using public key, obtaining original message, hashed result, hash algorithm. Client use the same algorithm to hash original message, and compared the result with the hashed result calculated by server. If they are the same, the message is intact.
* Even though hacker can modify message, we can use hash result as fingerprint to check if the message is intact


## Summary

PKI provides secure information transfer, used in either SSL(Secure Socket Layer) or TLS(Transport Layer Security). It involves 3 technologies:

* symmetric/asymmetric encryption: secured information transfer
* hash algorithm: data integrity
* digital certificate: server authentication, to prove the server is the authentic one

When you request a HTTPS connection to a webpage, the website will initially send its SSL certificate to your browser. This certificate contains the public key needed to begin the secure session. Based on this initial exchange, your browser and the website then initiate the ‘SSL handshake’. The SSL handshake involves the generation of shared secrets to establish a uniquely secure connection between yourself and the website.

When a trusted SSL Digital Certificate is used during a HTTPS connection, users will see a padlock icon in the browser address bar. When an Extended Validation Certificate is installed on a web site, the address bar will turn green.




## 重新设计

我们做一个思想实验，从最原始的「对称加密」开始讨论，分析其问题，然后得到新的解决方案，一个一个方案递进，然后最后推导到我们现在使用的**网络安全传输的方案**。

核心需要解决的问题是： 1）信息私密性 2）身份认证 3）信息完整性

### 1.对称加密

具体方案是双方都拿一个「密码本」，然后根据「密码本」来加密解密。

问题是，在没有「密码本」时，如何把「密码本」安全传给对方呢？

中间可能会被劫走。

### 2. 非对称加密 RSA 

我们想要发明一种算法，「加密算法」和「加密算法」可以不依赖同一本密码本。

举个例子，我们有两个人物，小明和小黑，小黑通过「加密算法」发送消息给小明，小明通过「解密算法」来给这个解密。我们希望「加密算法」公开的，加完密的消息，没有「解密算法」是无法解开。这样，小明想到得到的消息是加密的，且只有可以解密，那么只要把「解密算法」私有，「加密算法」公开即可。

这个算法，就是「**RSA**」。

效果是，问题1中「密码本」就不存在安全传输的问题了，因为「加密算法」的密码本是公开的。

那有了新**问题**，小黑如何知道是**真正**的小明，给他发的「加密算法」呢？如果是假的，那小黑的消息也会被发给坏人 —— 假的小明。

### 3. 数字签名 

现在我们需要认证身份的方式，就像**身份证**一样，上面有你的照片和身份证号，我看一下你的身份证，然后到「认证」的公安局查一下身份号，一看照片**一样**，就确认你是真的。

举个例子，浏览器访问网站「bank.com」, 然后「bank.com」提供了一个「证书」—— 网站名 + 一段被加密过的信息。然后我们的浏览器出厂时就保存了认证的「解密算法」，然后我们通过「解密算法」解密信息，得到的网站名是一样的，我们就确认了网站是真的。因为「解密算法」和「加密算法」是配对的。这个「解密算法」复原的消息，是无法通过其他「加密算法」来加密得到「证书」现实消息。

这个「证书」，就是数字签名。

效果是，我们解决了身份认证的问题了。只要我对每一个服务器都进行「身份认证」就可以了。

但是实际的问题是，太费钱费时，因为世界那么多服务器，一个银行，就对应那么多人的客户。

### 4. 非对称加密 + 对称加密

我们可以利用各自的优点，我们需要对银行进行认证，然后客户用RSA算法，让银行提供一个公开的「加密算法」，然后客户给银行，发一个「密码本」，然后之后就用「密码本」进行加密解密交流就可以了。

效果是，银行和客户的交流渠道就建立起来的。

新的问题来了，「坏了」读不懂内容，但是可以篡改内容，或许被「解密算法」解密之后还是有意义的信息。


### 5. 数据完整性 

所以，我们需要一种确认数据完整性的方式。

方案就是，给一个信息加一个「指纹」，这个「指纹」由「加密算法」加密「信息」得到。这样，整个信息就变了「原文」+ 「指纹」。 对方收到「消息」之后，用自己的「私钥」解密之后，再用公共的「加密算法」对「原文」加密得到一个「指纹」，然后对比两者，看看是否是一样。

效果是，我们就可以确认信息是否完整了。

## Reference 

* [数字证书原理](http://www.cnblogs.com/JeffreySun/archive/2010/06/24/1627247.html) : 详细阐述了相关的原理
* [@caomingkai](https://caomingkai.github.io/2018/12/28/Cryptography-PKI-public-key-infrastructure/) 
* https://www.instantssl.com/ssl-certificate-products/https.html
* https://en.wikipedia.org/wiki/Public_key_infrastructure

