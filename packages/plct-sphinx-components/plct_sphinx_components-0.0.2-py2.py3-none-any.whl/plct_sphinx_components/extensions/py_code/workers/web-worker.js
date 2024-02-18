/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/py-code/web-worker.js":
/*!***********************************!*\
  !*** ./src/py-code/web-worker.js ***!
  \***********************************/
/***/ (() => {

eval("if( 'undefined' === typeof window){\r\n    importScripts(\"https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js\");\r\n} \r\n\r\nvar pyodide = null;\r\nvar id = null;\r\n\r\nconst reactPyModule = {\r\n    getInput: (id, prompt) => {\r\n        const request = new XMLHttpRequest()\r\n        request.open('GET', `/py-get-input/?id=${id}&prompt=${prompt}`, false)\r\n        request.send(null)\r\n        return request.responseText\r\n    }\r\n}\r\n\r\nself.onmessage = async function (event) {\r\n    if(event.data.type === \"ID\"){\r\n        id = event.data.id;\r\n        await setupPyodide();\r\n    }\r\n    if (event.data.type === \"INSTALL\") {\r\n        id = event.data.id;\r\n        await install_package(event.data.packages);\r\n        self.postMessage({ type: \"PACKAGES_INSTALLED\" });\r\n    }\r\n\r\n    if (event.data.type === \"RUN\") {\r\n        try{\r\n            pyodide.runPython(`run_code('''${event.data.code}''')`)\r\n        }catch(e){\r\n            self.postMessage({ type: \"ERR\" })\r\n        }\r\n        finally{\r\n            self.postMessage({ type: \"CODE_EXECUTED\" });\r\n        }\r\n    }\r\n}\r\n\r\nasync function install_package(packages) {\r\n    const micropip = pyodide.pyimport('micropip')\r\n    packages.forEach(async (p) => {\r\n        await micropip.install(p)\r\n    });\r\n}\r\n\r\nasync function setupPyodide() {\r\n    pyodide = await self.loadPyodide({\r\n        stdout: (text) => {\r\n            self.postMessage({ type: \"STDOUT\", text: text })\r\n        },\r\n        stderr: (text) => {\r\n            self.postMessage({ type: \"STDERR\", text: text })\r\n        }\r\n    });\r\n    await pyodide.loadPackage(['pyodide-http'])\r\n    await pyodide.loadPackage(['micropip'])\r\n    pyodide.registerJsModule('react_py', reactPyModule)\r\n\r\n    const initCode = `\r\nimport pyodide_http\r\npyodide_http.patch_all()\r\n`\r\n    await pyodide.runPythonAsync(initCode)\r\n    \r\n    const patchInputCode = `\r\nimport sys, builtins\r\nimport react_py\r\n__prompt_str__ = \"\"\r\ndef get_input(prompt=\"\"):\r\n    global __prompt_str__\r\n    __prompt_str__ = prompt\r\n    print(prompt)\r\n    s = react_py.getInput(\"${id}\", prompt)\r\n    print(s)\r\n    return s\r\nbuiltins.input = get_input\r\nsys.stdin.readline = lambda: react_py.getInput(\"${id}\", __prompt_str__)\r\n`\r\n    await pyodide.runPythonAsync(patchInputCode)\r\n\r\n    const patchOutputCode = `\r\nimport sys, io, traceback\r\ndef run_code(code):\r\n  try:\r\n      exec(code, {})\r\n  except:\r\n      tb = traceback.format_exc().split(\"\\\\n\")\r\n      tb = tb[:1] + tb[2:] # Remove run_code from traceback\r\n      print(\"\\\\n\".join(tb))\r\n      raise\r\n`\r\n    await pyodide.runPythonAsync(patchOutputCode);\r\n    \r\n    self.postMessage({ type: \"PYODIDE_READY\" });\r\n}\r\n\r\n\r\n\r\n\r\n\n\n//# sourceURL=webpack://petljawebcomponents/./src/py-code/web-worker.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./src/py-code/web-worker.js"]();
/******/ 	
/******/ })()
;