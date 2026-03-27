local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")
local camera = workspace.CurrentCamera

local screenGui = Instance.new("ScreenGui")
screenGui.Name = "TargetIndicatorGui"
screenGui.ResetOnSpawn = false
screenGui.DisplayOrder = 999999999 
screenGui.IgnoreGuiInset = true 
screenGui.Parent = playerGui

local indicator = Instance.new("Frame")
indicator.Size = UDim2.fromOffset(25, 25) 
indicator.Position = UDim2.new(0, 0, 1, -25) 
indicator.BackgroundColor3 = Color3.fromRGB(170, 0, 255)
indicator.BorderSizePixel = 0
indicator.ZIndex = 999999999
indicator.Visible = false
indicator.Parent = screenGui

local controlPanel = Instance.new("Frame")
controlPanel.Size = UDim2.fromOffset(200, 270)
controlPanel.Position = UDim2.new(0.5, -100, 0.5, -135)
controlPanel.BackgroundColor3 = Color3.fromRGB(40, 40, 40)
controlPanel.BorderSizePixel = 2
controlPanel.Active = true
controlPanel.Parent = screenGui

local titleLabel = Instance.new("TextLabel")
titleLabel.Size = UDim2.new(1, 0, 0, 30)
titleLabel.BackgroundColor3 = Color3.fromRGB(20, 20, 20)
titleLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
titleLabel.Text = "Auto Shoot Settings"
titleLabel.Parent = controlPanel

local chanceLabel = Instance.new("TextLabel")
chanceLabel.Size = UDim2.fromOffset(100, 30)
chanceLabel.Position = UDim2.fromOffset(10, 40)
chanceLabel.BackgroundTransparency = 1
chanceLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
chanceLabel.Text = "Head Chance %:"
chanceLabel.TextXAlignment = Enum.TextXAlignment.Left
chanceLabel.Parent = controlPanel

local chanceBox = Instance.new("TextBox")
chanceBox.Size = UDim2.fromOffset(70, 30)
chanceBox.Position = UDim2.fromOffset(120, 40)
chanceBox.BackgroundColor3 = Color3.fromRGB(60, 60, 60)
chanceBox.TextColor3 = Color3.fromRGB(255, 255, 255)
chanceBox.Text = "100"
chanceBox.Parent = controlPanel

local bodyChanceLabel = Instance.new("TextLabel")
bodyChanceLabel.Size = UDim2.fromOffset(100, 30)
bodyChanceLabel.Position = UDim2.fromOffset(10, 80)
bodyChanceLabel.BackgroundTransparency = 1
bodyChanceLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
bodyChanceLabel.Text = "Body Chance %:"
bodyChanceLabel.TextXAlignment = Enum.TextXAlignment.Left
bodyChanceLabel.Parent = controlPanel

local bodyChanceBox = Instance.new("TextBox")
bodyChanceBox.Size = UDim2.fromOffset(70, 30)
bodyChanceBox.Position = UDim2.fromOffset(120, 80)
bodyChanceBox.BackgroundColor3 = Color3.fromRGB(60, 60, 60)
bodyChanceBox.TextColor3 = Color3.fromRGB(255, 255, 255)
bodyChanceBox.Text = "100"
bodyChanceBox.Parent = controlPanel

local holdLabel = Instance.new("TextLabel")
holdLabel.Size = UDim2.fromOffset(100, 30)
holdLabel.Position = UDim2.fromOffset(10, 120)
holdLabel.BackgroundTransparency = 1
holdLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
holdLabel.Text = "Hold Time (s):"
holdLabel.TextXAlignment = Enum.TextXAlignment.Left
holdLabel.Parent = controlPanel

local holdBox = Instance.new("TextBox")
holdBox.Size = UDim2.fromOffset(70, 30)
holdBox.Position = UDim2.fromOffset(120, 120)
holdBox.BackgroundColor3 = Color3.fromRGB(60, 60, 60)
holdBox.TextColor3 = Color3.fromRGB(255, 255, 255)
holdBox.Text = "0"
holdBox.Parent = controlPanel

local teamCheckButton = Instance.new("TextButton")
teamCheckButton.Size = UDim2.fromOffset(180, 30)
teamCheckButton.Position = UDim2.fromOffset(10, 160)
teamCheckButton.BackgroundColor3 = Color3.fromRGB(60, 60, 60)
teamCheckButton.TextColor3 = Color3.fromRGB(255, 0, 0)
teamCheckButton.Text = "Team Check: OFF"
teamCheckButton.Parent = controlPanel

local toggleLabel = Instance.new("TextLabel")
toggleLabel.Size = UDim2.new(1, -20, 0, 30)
toggleLabel.Position = UDim2.fromOffset(10, 200)
toggleLabel.BackgroundTransparency = 1
toggleLabel.TextColor3 = Color3.fromRGB(0, 255, 0)
toggleLabel.Text = "Status: ON (B to Toggle)"
toggleLabel.Parent = controlPanel

local infoLabel = Instance.new("TextLabel")
infoLabel.Size = UDim2.new(1, -20, 0, 30)
infoLabel.Position = UDim2.fromOffset(10, 230)
infoLabel.BackgroundTransparency = 1
infoLabel.TextColor3 = Color3.fromRGB(200, 200, 200)
infoLabel.Text = "Press J to hide menu"
infoLabel.Parent = controlPanel

local teamCheckEnabled = false

teamCheckButton.MouseButton1Click:Connect(function()
    teamCheckEnabled = not teamCheckEnabled
    if teamCheckEnabled then
        teamCheckButton.Text = "Team Check: ON"
        teamCheckButton.TextColor3 = Color3.fromRGB(0, 255, 0)
    else
        teamCheckButton.Text = "Team Check: OFF"
        teamCheckButton.TextColor3 = Color3.fromRGB(255, 0, 0)
    end
end)

local dragging = false
local dragInput, mousePos, framePos

controlPanel.InputBegan:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch then
        dragging = true
        mousePos = input.Position
        framePos = controlPanel.Position
        
        input.Changed:Connect(function()
            if input.UserInputState == Enum.UserInputState.End then
                dragging = false
            end
        end)
    end
end)

controlPanel.InputChanged:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseMovement or input.UserInputType == Enum.UserInputType.Touch then
        dragInput = input
    end
end)

UserInputService.InputChanged:Connect(function(input)
    if input == dragInput and dragging then
        local delta = input.Position - mousePos
        controlPanel.Position = UDim2.new(framePos.X.Scale, framePos.X.Offset + delta.X, framePos.Y.Scale, framePos.Y.Offset + delta.Y)
    end
end)

local botEnabled = true

UserInputService.InputBegan:Connect(function(input, gameProcessed)
    if gameProcessed then return end
    
    if input.KeyCode == Enum.KeyCode.J then
        controlPanel.Visible = not controlPanel.Visible
    elseif input.KeyCode == Enum.KeyCode.B then
        botEnabled = not botEnabled
        if botEnabled then
            toggleLabel.Text = "Status: ON (B to Toggle)"
            toggleLabel.TextColor3 = Color3.fromRGB(0, 255, 0)
        else
            toggleLabel.Text = "Status: OFF (B to Toggle)"
            toggleLabel.TextColor3 = Color3.fromRGB(255, 0, 0)
            indicator.Visible = false
        end
    end
end)

local hitbox = Instance.new("Part")
hitbox.Color = Color3.fromRGB(255, 0, 0)
hitbox.Material = Enum.Material.Neon
hitbox.Transparency = 0.5
hitbox.CanCollide = false
hitbox.CanTouch = false
hitbox.CanQuery = false
hitbox.Massless = true
hitbox.Anchored = true
hitbox.Parent = workspace

local raycastParams = RaycastParams.new()
raycastParams.FilterType = Enum.RaycastFilterType.Exclude

local keyStartTime = 0
local isHoldingKey = false

local currentTargetChar = nil
local wasHeadHit = false
local currentRollSuccess = false

local function CheckEnemy(targetPlayer)
    if not teamCheckEnabled then return true end
    if not targetPlayer then return true end
    if player.Neutral or targetPlayer.Neutral then return true end
    
    if player.Team ~= nil and targetPlayer.Team ~= nil then
        return player.Team ~= targetPlayer.Team
    end
    
    return player.TeamColor ~= targetPlayer.TeamColor
end

RunService.RenderStepped:Connect(function()
    local character = player.Character
    if not character then 
        hitbox.Transparency = 1
        indicator.Visible = false
        currentTargetChar = nil
        wasHeadHit = false
        currentRollSuccess = false
        return 
    end

    hitbox.Transparency = 0.5
    
    local origin = camera.CFrame.Position
    local direction = camera.CFrame.LookVector * 10000
    
    local hitDistance = 10000
    local isEnemyConfirmed = false
    local isHeadHit = false
    local hitPart = nil
    local characterModel = nil
    local finalPosition = origin + direction

    local ignoreList = {character, hitbox}
    
    for i = 1, 15 do
        raycastParams.FilterDescendantsInstances = ignoreList
        local result = workspace:Raycast(origin, direction, raycastParams)
        
        if result then
            local instName = string.lower(result.Instance.Name)
            if instName == "humanoidrootpart" or result.Instance.Transparency >= 0.8 or string.match(instName, "arm") or string.match(instName, "leg") or string.match(instName, "hand") or string.match(instName, "foot") then
                table.insert(ignoreList, result.Instance)
            else
                hitPart = result.Instance
                hitDistance = result.Distance
                finalPosition = result.Position
                break
            end
        else
            break
        end
    end
    
    if hitPart then
        local current = hitPart
        local humanoid = nil
        
        while current and current ~= workspace do
            humanoid = current:FindFirstChildOfClass("Humanoid")
            if humanoid then
                characterModel = current
                break
            end
            current = current.Parent
        end
        
        if characterModel and characterModel ~= character and humanoid.Health > 0 then
            local targetPlayer = Players:GetPlayerFromCharacter(characterModel)
            
            isEnemyConfirmed = CheckEnemy(targetPlayer)
            
            if isEnemyConfirmed then
                local pName = string.lower(hitPart.Name)
                if string.match(pName, "head") or hitPart:FindFirstAncestorOfClass("Accessory") or hitPart:FindFirstAncestorOfClass("Hat") then
                    isHeadHit = true
                else
                    isHeadHit = false
                end
            end
        end
    end
    
    hitbox.Size = Vector3.new(0.1, 0.1, hitDistance)
    hitbox.CFrame = camera.CFrame * CFrame.new(0, 0, -hitDistance / 2)
    
    if UserInputService:IsKeyDown(Enum.KeyCode.N) then
        if not isHoldingKey then
            isHoldingKey = true
            keyStartTime = os.clock()
        end
    else
        isHoldingKey = false
        keyStartTime = 0 
    end
    
    local holdTimeRequired = tonumber(holdBox.Text) or 0
    local hasHeldLongEnough = isHoldingKey and (os.clock() - keyStartTime >= holdTimeRequired)
    
    if botEnabled and hasHeldLongEnough and isEnemyConfirmed then
        local needsImmediateRoll = false
        
        if characterModel ~= currentTargetChar then
            needsImmediateRoll = true
        elseif isHeadHit ~= wasHeadHit then
            needsImmediateRoll = true
        end
        
        if needsImmediateRoll then
            currentTargetChar = characterModel
            wasHeadHit = isHeadHit
            
            local chanceToHit = isHeadHit and (tonumber(chanceBox.Text) or 100) or (tonumber(bodyChanceBox.Text) or 100)
            currentRollSuccess = (math.random(1, 100) <= math.clamp(chanceToHit, 0, 100))
        end
        
        indicator.Visible = currentRollSuccess
    else
        currentTargetChar = nil
        wasHeadHit = false
        currentRollSuccess = false
        indicator.Visible = false
    end
end)
