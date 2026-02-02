import React, { useState } from 'react';
import { Shield, Check, X, RefreshCw, Copy, Eye, EyeOff } from 'lucide-react';

function ValidationItem({ label, passed }) {
  return (
    <div className="flex items-center">
      {passed ? (
        <Check className="w-5 h-5 text-green-600 mr-2 flex-shrink-0" />
      ) : (
        <X className="w-5 h-5 text-red-600 mr-2 flex-shrink-0" />
      )}
      <span className={`text-sm ${passed ? 'text-green-700' : 'text-red-700'}`}>
        {label}
      </span>
    </div>
  );
}

export default function PasswordValidator() {
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [validation, setValidation] = useState(null);
  const [generatedPassword, setGeneratedPassword] = useState('');
  const [passwordLength, setPasswordLength] = useState(12);
  const [copied, setCopied] = useState(false);

  const validatePassword = (pwd) => {
    const hasLowercase = /[a-z]/.test(pwd);
    const hasUppercase = /[A-Z]/.test(pwd);
    const hasDigit = /[0-9]/.test(pwd);
    const hasSpecial = /[]!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(pwd);
    const isLongEnough = pwd.length >= 8;
    const isStrong = hasLowercase && hasUppercase && hasDigit && hasSpecial && isLongEnough;
    return {
      isStrong,
      checks: {
        length: isLongEnough,
        lowercase: hasLowercase,
        uppercase: hasUppercase,
        digit: hasDigit,
        special: hasSpecial
      }
    };
  };

  const generateStrongPassword = (length) => {
    const lowercase = 'abcdefghijklmnopqrstuvwxyz';
    const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const digits = '0123456789';
    const symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?';
    let pwd = [
      lowercase[Math.floor(Math.random() * lowercase.length)],
      uppercase[Math.floor(Math.random() * uppercase.length)],
      digits[Math.floor(Math.random() * digits.length)],
      symbols[Math.floor(Math.random() * symbols.length)]
    ];
    const allChars = lowercase + uppercase + digits + symbols;
    for (let i = 4; i < length; i++) {
      pwd.push(allChars[Math.floor(Math.random() * allChars.length)]);
    }
    for (let i = pwd.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [pwd[i], pwd[j]] = [pwd[j], pwd[i]];
    }
    return pwd.join('');
  };

  const handleValidate = () => {
    if (!password) {
      alert('Please enter a password to validate');
      return;
    }
    const result = validatePassword(password);
    setValidation(result);
    if (!result.isStrong) {
      const newPassword = generateStrongPassword(passwordLength);
      setGeneratedPassword(newPassword);
    } else {
      setGeneratedPassword('');
    }
  };

  const handleGenerate = () => {
    const newPassword = generateStrongPassword(passwordLength);
    setGeneratedPassword(newPassword);
    setValidation(null);
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-2xl p-8">
        <div className="flex items-center justify-center mb-8">
          <Shield className="w-12 h-12 text-indigo-600 mr-3" />
          <h1 className="text-4xl font-bold text-gray-800">Password Security</h1>
        </div>
        <div className="mb-6">
          <label className="block text-sm font-semibold text-gray-700 mb-2">
            Enter Your Password
          </label>
          <div className="relative">
            <input
              type={showPassword ? "text" : "password"}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter password to validate..."
              className="w-full px-4 py-3 pr-12 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500 transition"
            />
            <button
              onClick={() => setShowPassword(!showPassword)}
              className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-gray-700"
            >
              {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
            </button>
          </div>
        </div>
        <button
          onClick={handleValidate}
          className="w-full bg-indigo-600 text-white py-3 rounded-lg font-semibold hover:bg-indigo-700 transition mb-6 flex items-center justify-center"
        >
          <Shield className="w-5 h-5 mr-2" />
          Validate Password
        </button>
        {validation && (
          <div className={`mb-6 p-6 rounded-lg ${validation.isStrong ? 'bg-green-50 border-2 border-green-500' : 'bg-red-50 border-2 border-red-500'}`}>
            <h2 className="text-xl font-bold mb-4 flex items-center">
              {validation.isStrong ? (
                <React.Fragment>
                  <Check className="w-6 h-6 text-green-600 mr-2" />
                  <span className="text-green-700">Strong Password!</span>
                </React.Fragment>
              ) : (
                <React.Fragment>
                  <X className="w-6 h-6 text-red-600 mr-2" />
                  <span className="text-red-700">Password Not Strong Enough</span>
                </React.Fragment>
              )}
            </h2>
            <div className="space-y-2">
              <ValidationItem label="Minimum 8 characters" passed={validation.checks.length} />
              <ValidationItem label="Contains lowercase letters" passed={validation.checks.lowercase} />
              <ValidationItem label="Contains uppercase letters" passed={validation.checks.uppercase} />
              <ValidationItem label="Contains numbers" passed={validation.checks.digit} />
              <ValidationItem label="Contains special characters" passed={validation.checks.special} />
            </div>
          </div>
        )}
        {(generatedPassword || (!validation)) && (
          <div className="bg-gradient-to-r from-purple-50 to-indigo-50 p-6 rounded-lg border-2 border-indigo-200">
            <h2 className="text-xl font-bold text-gray-800 mb-4">Generate Strong Password</h2>
            <div className="mb-4">
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                Password Length: {passwordLength}
              </label>
              <input
                type="range"
                min="8"
                max="32"
                value={passwordLength}
                onChange={(e) => setPasswordLength(parseInt(e.target.value))}
                className="w-full h-2 bg-indigo-200 rounded-lg appearance-none cursor-pointer"
              />
            </div>
            <button
              onClick={handleGenerate}
              className="w-full bg-gradient-to-r from-purple-600 to-indigo-600 text-white py-3 rounded-lg font-semibold hover:from-purple-700 hover:to-indigo-700 transition mb-4 flex items-center justify-center"
            >
              <RefreshCw className="w-5 h-5 mr-2" />
              Generate Password
            </button>
            {generatedPassword && (
              <div className="bg-white p-4 rounded-lg border-2 border-indigo-300">
                <div className="flex items-center justify-between">
                  <code className="text-lg font-mono text-gray-800 break-all flex-1">
                    {generatedPassword}
                  </code>
                  <button
                    onClick={() => copyToClipboard(generatedPassword)}
                    className="ml-3 p-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition flex-shrink-0"
                    title="Copy to clipboard"
                  >
                    <Copy className="w-5 h-5" />
                  </button>
                </div>
                {copied && (
                  <p className="text-green-600 text-sm mt-2 text-center font-semibold">
                         Copied to clipboard!
                  </p>
                )}
              </div>
            )}
          </div>
        )}
        <div className="mt-6 bg-yellow-50 p-4 rounded-lg border border-yellow-200">
          <p className="text-sm text-yellow-800">
            <strong> Tip:</strong> Save your password in a secure password manager and never share it with anyone!
          </p>
        </div>
      </div>
    </div>
  );
}
```// filepath: c:\Users\Sandeep Patra\OneDrive\Documents\projects\frontend.jsx
import React, { useState } from 'react';
import { Shield, Check, X, RefreshCw, Copy, Eye, EyeOff } from 'lucide-react';

function ValidationItem({ label, passed }) {
  return (
    <div className="flex items-center">
      {passed ? (
        <Check className="w-5 h-5 text-green-600 mr-2 flex-shrink-0" />
      ) : (
        <X className="w-5 h-5 text-red-600 mr-2 flex-shrink-0" />
      )}
      <span className={`text-sm ${passed ? 'text-green-700' : 'text-red-700'}`}>
        {label}
      </span>
    </div>
  );
}

export default function PasswordValidator() {
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [validation, setValidation] = useState(null);
  const [generatedPassword, setGeneratedPassword] = useState('');
  const [passwordLength, setPasswordLength] = useState(12);
  const [copied, setCopied] = useState(false);

  const validatePassword = (pwd) => {
    const hasLowercase = /[a-z]/.test(pwd);
    const hasUppercase = /[A-Z]/.test(pwd);
    const hasDigit = /[0-9]/.test(pwd);
    const hasSpecial = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(pwd);
    const isLongEnough = pwd.length >= 8;
    const isStrong = hasLowercase && hasUppercase && hasDigit && hasSpecial && isLongEnough;
    return {
      isStrong,
      checks: {
        length: isLongEnough,
        lowercase: hasLowercase,
        uppercase: hasUppercase,
        digit: hasDigit,
        special: hasSpecial
      }
    };
  };

  const generateStrongPassword = (length) => {
    const lowercase = 'abcdefghijklmnopqrstuvwxyz';
    const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const digits = '0123456789';
    const symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?';
    let pwd = [
      lowercase[Math.floor(Math.random() * lowercase.length)],
      uppercase[Math.floor(Math.random() * uppercase.length)],
      digits[Math.floor(Math.random() * digits.length)],
      symbols[Math.floor(Math.random() * symbols.length)]
    ];
    const allChars = lowercase + uppercase + digits + symbols;
    for (let i = 4; i < length; i++) {
      pwd.push(allChars[Math.floor(Math.random() * allChars.length)]);
    }
    for (let i = pwd.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [pwd[i], pwd[j]] = [pwd[j], pwd[i]];
    }
    return pwd.join('');
  };

  const handleValidate = () => {
    if (!password) {
      alert('Please enter a password to validate');
      return;
    }
    const result = validatePassword(password);
    setValidation(result);
    if (!result.isStrong) {
      const newPassword = generateStrongPassword(passwordLength);
      setGeneratedPassword(newPassword);
    } else {
      setGeneratedPassword('');
    }
  };

  const handleGenerate = () => {
    const newPassword = generateStrongPassword(passwordLength);
    setGeneratedPassword(newPassword);
    setValidation(null);
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-2xl p-8">
        <div className="flex items-center justify-center mb-8">
          <Shield className="w-12 h-12 text-indigo-600 mr-3" />
          <h1 className="text-4xl font-bold text-gray-800">Password Security</h1>
        </div>
        <div className="mb-6">
          <label className="block text-sm font-semibold text-gray-700 mb-2">
            Enter Your Password
          </label>
          <div className="relative">
            <input
              type={showPassword ? "text" : "password"}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter password to validate..."
              className="w-full px-4 py-3 pr-12 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500 transition"
            />
            <button
              onClick={() => setShowPassword(!showPassword)}
              className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-gray-700"
            >
              {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
            </button>
          </div>
        </div>
        <button
          onClick={handleValidate}
          className="w-full bg-indigo-600 text-white py-3 rounded-lg font-semibold hover:bg-indigo-700 transition mb-6 flex items-center justify-center"
        >
          <Shield className="w-5 h-5 mr-2" />
          Validate Password
        </button>
        {validation && (
          <div className={`mb-6 p-6 rounded-lg ${validation.isStrong ? 'bg-green-50 border-2 border-green-500' : 'bg-red-50 border-2 border-red-500'}`}>
            <h2 className="text-xl font-bold mb-4 flex items-center">
              {validation.isStrong ? (
                <React.Fragment>
                  <Check className="w-6 h-6 text-green-600 mr-2" />
                  <span className="text-green-700">Strong Password!</span>
                </React.Fragment>
              ) : (
                <React.Fragment>
                  <X className="w-6 h-6 text-red-600 mr-2" />
                  <span className="text-red-700">Password Not Strong Enough</span>
                </React.Fragment>
              )}
            </h2>
            <div className="space-y-2">
              <ValidationItem label="Minimum 8 characters" passed={validation.checks.length} />
              <ValidationItem label="Contains lowercase letters" passed={validation.checks.lowercase} />
              <ValidationItem label="Contains uppercase letters" passed={validation.checks.uppercase} />
              <ValidationItem label="Contains numbers" passed={validation.checks.digit} />
              <ValidationItem label="Contains special characters" passed={validation.checks.special} />
            </div>
          </div>
        )}
        {(generatedPassword || (!validation)) && (
          <div className="bg-gradient-to-r from-purple-50 to-indigo-50 p-6 rounded-lg border-2 border-indigo-200">
            <h2 className="text-xl font-bold text-gray-800 mb-4">Generate Strong Password</h2>
            <div className="mb-4">
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                Password Length: {passwordLength}
              </label>
              <input
                type="range"
                min="8"
                max="32"
                value={passwordLength}
                onChange={(e) => setPasswordLength(parseInt(e.target.value))}
                className="w-full h-2 bg-indigo-200 rounded-lg appearance-none cursor-pointer"
              />
            </div>
            <button
              onClick={handleGenerate}
              className="w-full bg-gradient-to-r from-purple-600 to-indigo-600 text-white py-3 rounded-lg font-semibold hover:from-purple-700 hover:to-indigo-700 transition mb-4 flex items-center justify-center"
            >
              <RefreshCw className="w-5 h-5 mr-2" />
              Generate Password
            </button>
            {generatedPassword && (
              <div className="bg-white p-4 rounded-lg border-2 border-indigo-300">
                <div className="flex items-center justify-between">
                  <code className="text-lg font-mono text-gray-800 break-all flex-1">
                    {generatedPassword}
                  </code>
                  <button
                    onClick={() => copyToClipboard(generatedPassword)}
                    className="ml-3 p-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition flex-shrink-0"
                    title="Copy to clipboard"
                  >
                    <Copy className="w-5 h-5" />
                  </button>
                </div>
                {copied && (
                  <p className="text-green-600 text-sm mt-2 text-center font-semibold">
                         Copied to clipboard!
                  </p>
                )}
              </div>
            )}
          </div>
        )}
        <div className="mt-6 bg-yellow-50 p-4 rounded-lg border border-yellow-200">
          <p className="text-sm text-yellow-800">
            <strong> Tip:</strong> Save your password in a secure password manager and never share it with anyone!
          </p>
        </div>
      </div>
    </div>
  );
}