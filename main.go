package main

import (
	"fmt"
	"github.com/bitly/go-simplejson"
	"github.com/tealeg/xlsx"
	"io/ioutil"
	"os"
	"strings"
	"sync"
	"time"
)

const (
	//LUA_ROOT = `F:\Lua\Lua workspace\test_conf\`
	//LUA_ROOT = `F:\EGame_Trunk\server\scripts\lua\data\config.json\`
	LUA_ROOT = `Test\Lua\`
	//XLS_ROOT = `F:\go\project\src\xls2lua\`
	XLS_ROOT = `Test\`
)

var Config *simplejson.Json

type ColumnInfo struct {
	columnName string
	columnType string
	columnWay string
	columnData []string
}

type KeyInfo struct {
	currIndex string
	columnType string
	columnName string
	isFirst bool
	isLast bool
	keyPos int
}

func getXlsFileList() map[string]bool {
	infos, err := ioutil.ReadDir(XLS_ROOT)
	if err != nil {
		panic(err)
	}

	fileList := make(map[string]bool)
	for _, v := range infos {
		if v.IsDir() ||
			strings.Contains(v.Name(), `~$`) ||
			strings.Contains(v.Name(), "svn") {
			continue
		}

		split := strings.Split(v.Name(), ".")
		if len(split) != 2 {
			continue
		}

		if split[1] == "xlsx" || split[1] == "xls" {
			fileList[v.Name()] = true
		}
	}

	return fileList
}

func writeLuaFile(filename string, data []byte) {
	defer wg.Done()
	ioutil.WriteFile(filename, []byte(data), 755)
}

func genLua(fileName string){
	defer wg.Done()
	info := getXlsxInfo(fileName)
	tableName := strings.Split(fileName, ".")[0]
	writeData := fmt.Sprintf("%s = {}\n\n", tableName)
	fmt.Printf("File Name: %s \n", fileName)
	for sheetName, v := range info{
		writeData += getSheetData(sheetName, v, tableName, fileName)
	}

	wg.Add(1)
	go writeLuaFile(LUA_ROOT + tableName+".lua", []byte(writeData))
}

func getSheetData(sheetName string, columnInfo map[int]ColumnInfo, tableName string, fileName string) string {
	fmt.Printf("Sheet Name: %s\n", sheetName)
	// 获取 key 配置信息
	colSpaceStr := "\t"
	keyMap := make(map[string]KeyInfo)
	array, _ := Config.Get(fileName).Get(sheetName).Get("key").Array()
	for keyPos, keyName := range array {
		keyMap[keyName.(string)] = KeyInfo{keyPos: keyPos}
		if keyPos != len(array)-1 {
			colSpaceStr += "\t"
		}
	}

	// 组装 sheet 初始信息
	sheetData := fmt.Sprintf("------------------------------%s.%s%s--------------------------\n", tableName, strings.ToUpper(sheetName), "_CONFIG")
	sheetData += fmt.Sprintf("%s.%s%s = {\n", tableName, strings.ToUpper(sheetName), "_CONFIG")

	isSkip := true
	dataLen := len(columnInfo[len(columnInfo)-1].columnData)
	for rowNum := 0; rowNum < dataLen; rowNum++ {
		headStr := ""
		columnStr := ""
		isContinue := false
		colLen := len(columnInfo)
		for colNum := 0; colNum < colLen; colNum++ {
			// 判断导出方式
			if !strings.Contains(columnInfo[colNum].columnWay, "s") {
				continue
			}

			// 检测一下是否为指定的 key
			isSkip = false
			keyInfo, ok := keyMap[columnInfo[colNum].columnName]
			if ok {
				// 判断是否切换 key 值
				if columnInfo[colNum].columnData[rowNum] != keyInfo.currIndex {
						keyInfo.currIndex = columnInfo[colNum].columnData[rowNum]
						keyInfo.columnType = columnInfo[colNum].columnType
						keyInfo.columnName = columnInfo[colNum].columnName
						keyInfo.isFirst = true
				}

				// 判断是否为最后一个 key，用该 key 的值作为本行数据的下标（headStr）
				if keyInfo.keyPos == len(array)-1 {
					if columnInfo[colNum].columnData[rowNum] == "" {
						isContinue = true
						break
					}
					headStr = fmt.Sprintf("%s[ %s ] = {", colSpaceStr, ToLuaDataType(columnInfo[colNum].columnType, columnInfo[colNum].columnData[rowNum], sheetName, columnInfo[colNum].columnName))
				}

				// 判断是否为最后一行数据，用作特殊处理（"}"）
				if rowNum == dataLen-1 {
					keyInfo.isLast = true
				}
				keyMap[columnInfo[colNum].columnName] = keyInfo
			} else {
				// 没用配置 key 值的，默认使用第一个做主 key
				if colNum == 0 {
					if columnInfo[colNum].columnData[rowNum] == "" {
						isContinue = true
						break
					}
					headStr = fmt.Sprintf("%s[ %s ] = {", colSpaceStr, ToLuaDataType(columnInfo[colNum].columnType, columnInfo[colNum].columnData[rowNum], sheetName, columnInfo[colNum].columnName))
				}
			}

			// 检测是否为最后一列数据，用于去逗号
			if colNum == colLen-1 {
				columnStr += fmt.Sprintf("%s = %s", columnInfo[colNum].columnName, ToLuaDataType(columnInfo[colNum].columnType, columnInfo[colNum].columnData[rowNum], sheetName, columnInfo[colNum].columnName))
			} else {
				columnStr += fmt.Sprintf("%s = %s,", columnInfo[colNum].columnName, ToLuaDataType(columnInfo[colNum].columnType, columnInfo[colNum].columnData[rowNum], sheetName, columnInfo[colNum].columnName))
			}
		}
		// 一行数据的结束符
		columnStr += "},\n"

		// 跳过错误数据
		if isContinue {
			break
		}

		// 忽略没有数据的 sheet
		if isSkip {
			return ""
		}

		// 补齐尾部信息
		lastStr := ""
		for i := len(array)-2; i >= 0 ; i-- {
			keyInfo, ok := keyMap[array[i].(string)]
			if ok {
				spaceStr := ""
				for j := 0; j < i+1; j++ {
					spaceStr += "\t"
				}
				if keyInfo.isFirst {
					if rowNum != 0 {
						sheetData += fmt.Sprintf("%s},\n", spaceStr)
					}
				}

				if keyInfo.isLast {
					lastStr += fmt.Sprintf("%s},\n", spaceStr)
				}
			}
		}

		// 补齐多 key 情况下的头部信息
		for i := 0; i < len(array)-1; i++ {
			keyInfo, ok := keyMap[array[i].(string)]
			if ok {
				spaceStr := ""
				for j := 0; j < i+1; j++ {
					spaceStr += "\t"
				}
				if keyInfo.isFirst {
					sheetData += fmt.Sprintf("%s[ %s ] = {\n", spaceStr, ToLuaDataType(keyInfo.columnType, keyInfo.currIndex, sheetName, keyInfo.columnName))
					keyInfo.isFirst = false
					keyMap[array[i].(string)] = keyInfo
				}
			}
		}
		//fmt.Println(columnStr)
		sheetData += headStr + columnStr + lastStr
	}

	sheetData += "}\n\n"
	return sheetData
}
func ToLuaDataType(columnType string, columnData string, sheetName string, keyName string) string {
	if keyName == "aiTreeJson" && sheetName == "AIJson"{
		return 	"[[" + columnData + "]]"
	}

	if columnType == "string" {
		return `'` + columnData + `'`
	}

	if columnData == "" && (columnType == "int" || columnType == "float"){
		return "0"
	}

	return columnData
}

func getXlsxInfo(fileName string) map[string]map[int]ColumnInfo {
	//fmt.Printf("XLS_ROOT:%s, fileName:%s \n", XLS_ROOT, fileName)
	file, err := xlsx.OpenFile(XLS_ROOT + fileName)
	if err != nil {
		showErrorMsg(err.Error())
	}
	typeDict := make(map[string]map[int]ColumnInfo)
	for _, sheet := range file.Sheets {
		if sheet.Name[0] == '_' {
			continue
		}

		typeDict[sheet.Name] = make(map[int]ColumnInfo)
		for cIndex := 0; cIndex < len(sheet.Rows); cIndex++ {
			flagStr := ""
			for rIndex := 0; rIndex < len(sheet.Rows[cIndex].Cells); rIndex++ {
				if cIndex == 0 { // 列类型名
					if sheet.Rows[cIndex].Cells[rIndex].String() == "" {
						break
					}
					columnInfo, ok := typeDict[sheet.Name][rIndex]
					if !ok {
						columnInfo = ColumnInfo{}
					}
					columnInfo.columnName = sheet.Rows[cIndex].Cells[rIndex].String()
					typeDict[sheet.Name][rIndex] = columnInfo
				}

				if cIndex == 1 { // 列类型
					columnInfo, ok := typeDict[sheet.Name][rIndex]
					if ok {
						columnInfo.columnType = sheet.Rows[cIndex].Cells[rIndex].String()
						typeDict[sheet.Name][rIndex] = columnInfo
					}
				}

				if cIndex == 3 { // 列导出方式(cs)
					columnInfo, ok := typeDict[sheet.Name][rIndex]
					if ok {
						columnInfo.columnWay = sheet.Rows[cIndex].Cells[rIndex].String()
						typeDict[sheet.Name][rIndex] = columnInfo
					}
				}

				if cIndex > 3 { // 列数据
					columnInfo, ok := typeDict[sheet.Name][rIndex]
					if ok {
						columnInfo.columnData = append(columnInfo.columnData, sheet.Rows[cIndex].Cells[rIndex].String())
						typeDict[sheet.Name][rIndex] = columnInfo
					}
				}
				flagStr += sheet.Rows[cIndex].Cells[rIndex].String()
			}

			// 过滤掉无用的行数据
			if flagStr == ""{
				for rIndex := 0; rIndex < len(sheet.Rows[cIndex].Cells); rIndex++ {
					columnInfo, ok := typeDict[sheet.Name][rIndex]
					if ok {
						columnInfo.columnData = columnInfo.columnData[:len(columnInfo.columnData)-1]
						typeDict[sheet.Name][rIndex] = columnInfo
					}
				}
				break
			}
		}
	}

	return typeDict
}
var wg sync.WaitGroup
func process(fileName string){
	fileMap := getXlsFileList()
	if fileName == "all" {
		for _fileName := range fileMap{
			wg.Add(1)
			go genLua(_fileName)
		}
		wg.Wait()
	}else {
		if !fileMap[fileName] {
			showErrorMsg(fmt.Sprintf("找不到指定文件：%s", fileName))
		}
		wg.Add(1)
		go genLua(fileName)
		wg.Wait()
	}
}

func readPyConfig() {
	readFile, err := ioutil.ReadFile("config.py")
	if err != nil {
		showErrorMsg(err.Error())
	}

	readStr := string(readFile)
	start := strings.Index(readStr, "{")
	end := strings.LastIndex(readStr, "}")
	readStr = strings.Replace(readStr, `'`, `"`, -1)
	//fmt.Println(readStr[start:end+1])
	newJson, err := simplejson.NewJson([]byte(readStr[start:end+1]))
	if err != nil {
		showErrorMsg(err.Error())
	}
	Config = newJson
}

func readJsonConfig() {
	readFile, err := ioutil.ReadFile("config.json")
	if err != nil {
		showErrorMsg(err.Error())
	}

	readStr := string(readFile)

	newJson, err := simplejson.NewJson([]byte(readStr))
	if err != nil {
		showErrorMsg(err.Error())
	}
	Config = newJson
}

func showErrorMsg(format string, params ...interface{})  {
	fmt.Printf(format, params...)
	os.Exit(1)
}

func main() {
	fileName := "all"
	//fileName := "GemConf.xlsx"
	//fileName := "Discount.xlsx"
	//fileName := "Trade.xlsx"
	process(fileName)
	fmt.Println(time.Since(startTime))
}

var startTime = time.Now()

func init()  {
	startTime = time.Now()
	//readPyConfig()
	readJsonConfig()
}