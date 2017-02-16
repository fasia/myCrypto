using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using WpfAppCryptography.ViewModel;
namespace WpfAppCryptography.Algorithms.TechniqueBased.Substitution
{
    public class MonoAlphabeticCipher : Algorithm
    {
        public new string AlgorithmName = "Mono Alphabetic Cipher";

        private char[] o = new char[] { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
        private char[] m = new char[] { 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm' };

        private int GetIndex(char ch, char[] ca)
        {
            int i, result = 0;
            for (i = 0; i < 26; ++i)
            {
                if (ca[i] == ch)
                {
                    result = i;
                    break;
                }
            }
            return result;
        }

        public override string Decrypt(string ciphertext, string key)
        {
            int i, j;
            string plaintext = null;
            char[] ctca = ciphertext.ToCharArray();
            char[] cc = new char[500];
            for (i = 0; i < ctca.Length; ++i)
            {
                if (ctca[i] == ' ')
                {
                    cc[i] = ctca[i];
                }
                else
                {
                    j = GetIndex(ctca[i], m);
                    cc[i] = o[j];
                }
                plaintext += cc[i];
            }
            return plaintext;
        }

        public override string Encrypt(string plaintext, string key)
        {
            int i, j;
            string ciphertext = null;
            char[] ptca = plaintext.ToCharArray();
            char[] cc = new char[500];
            for (i = 0; i < ptca.Length; ++i)
            {
                if (ptca[i] == ' ')
                {
                    cc[i] = ptca[i];
                }
                else
                {
                    j = GetIndex(ptca[i],o);
                    cc[i] = m[j];
                }
                ciphertext += cc[i];
            }
            return ciphertext;
        }
    }
}