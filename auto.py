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
controlPanel.Size = UDim2.fromOffset(200, 230)
controlPanel.Position = UDim2.new(0.5, -100, 0.5, -115)
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

local delayLabel = Instance.new("TextLabel")
delayLabel.Size = UDim2.fromOffset(100, 30)
delayLabel.Position = UDim2.fromOffset(10, 40)
delayLabel.BackgroundTransparency = 1
delayLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
delayLabel.Text = "Flash Delay:"
delayLabel.TextXAlignment = Enum.TextXAlignment.Left
delayLabel.Parent = controlPanel

local delayBox = Instance.new("TextBox")
delayBox.Size = UDim2.fromOffset(70, 30)
delayBox.Position = UDim2.fromOffset(120, 40)
delayBox.BackgroundColor3 = Color3.fromRGB(60, 60, 60)
delayBox.TextColor3 = Color3.fromRGB(255, 255, 255)
delayBox.Text = "0.3"
delayBox.Parent = controlPanel

local chanceLabel = Instance.new("TextLabel")
chanceLabel.Size = UDim2.fromOffset(100, 30)
chanceLabel.Position = UDim2.fromOffset(10, 80)
chanceLabel.BackgroundTransparency = 1
chanceLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
chanceLabel.Text = "Hit Chance %:"
chanceLabel.TextXAlignment = Enum.TextXAlignment.Left
chanceLabel.Parent = controlPanel

local chanceBox = Instance.new("TextBox")
chanceBox.Size = UDim2.fromOffset(70, 30)
chanceBox.Position = UDim2.fromOffset(120, 80)
chanceBox.BackgroundColor3 = Color3.fromRGB(60, 60, 60)
chanceBox.TextColor3 = Color3.fromRGB(255, 255, 255)
chanceBox.Text = "100"
chanceBox.Parent = controlPanel

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
holdBox.Text = "0.3"
holdBox.Parent = controlPanel

local toggleLabel = Instance.new("TextLabel")
toggleLabel.Size = UDim2.new(1, -20, 0, 30)
toggleLabel.Position = UDim2.fromOffset(10, 160)
toggleLabel.BackgroundTransparency = 1
toggleLabel.TextColor3 = Color3.fromRGB(0, 255, 0)
toggleLabel.Text = "Status: ON (B to Toggle)"
toggleLabel.Parent = controlPanel

local infoLabel = Instance.new("TextLabel")
infoLabel.Size = UDim2.new(1, -20, 0, 30)
infoLabel.Position = UDim2.fromOffset(10, 190)
infoLabel.BackgroundTransparency = 1
infoLabel.TextColor3 = Color3.fromRGB(200, 200, 200)
infoLabel.Text = "Press N to hide menu"
infoLabel.Parent = controlPanel

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
    
    if input.KeyCode == Enum.KeyCode.N then
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

local isFlashing = false
local rightClickStartTime = 0
local isHoldingRightClick = false
local currentTargetFound = false 

RunService.RenderStepped:Connect(function()
    local character = player.Character
    if not character then 
        hitbox.Transparency = 1
        indicator.Visible = false
        isFlashing = false
        currentTargetFound = false
        return 
    end

    hitbox.Transparency = 0.5
    raycastParams.FilterDescendantsInstances = {character, hitbox}
    
    local origin = camera.CFrame.Position
    local direction = camera.CFrame.LookVector * 10000
    
    local result = workspace:Raycast(origin, direction, raycastParams)
    
    local hitDistance = 10000
    local targetFound = false
    
    if result then
        hitDistance = result.Distance
        if result.Instance then
            local model = result.Instance:FindFirstAncestorOfClass("Model")
            if model then
                local humanoid = model:FindFirstChildOfClass("Humanoid")
                local targetPlayer = Players:GetPlayerFromCharacter(model)
                
                if humanoid and humanoid.Health > 0 and targetPlayer and targetPlayer ~= player then
                    if targetPlayer.Team == nil or targetPlayer.Team ~= player.Team then
                        targetFound = true
                    end
                end
            end
        end
    end
    
    currentTargetFound = targetFound 
    
    hitbox.Size = Vector3.new(0.5, 0.5, hitDistance)
    hitbox.CFrame = camera.CFrame * CFrame.new(0, 0, -hitDistance / 2)
    
    if UserInputService:IsMouseButtonPressed(Enum.UserInputType.MouseButton2) then
        if not isHoldingRightClick then
            isHoldingRightClick = true
            rightClickStartTime = os.clock()
        end
    else
        isHoldingRightClick = false
        rightClickStartTime = 0 
    end
    
    local holdTimeRequired = tonumber(holdBox.Text) or 0.3
    local hasHeldLongEnough = isHoldingRightClick and (os.clock() - rightClickStartTime >= holdTimeRequired)
    
    if botEnabled and targetFound and hasHeldLongEnough and not isFlashing then
        isFlashing = true
        
        local currentDelay = tonumber(delayBox.Text) or 0.3
        local chanceToHit = tonumber(chanceBox.Text) or 100
        chanceToHit = math.clamp(chanceToHit, 0, 100)
        
        local roll = math.random(1, 100)
        local isHit = roll <= chanceToHit
        
        local function triggerFlash()
            indicator.Visible = true
            task.delay(currentDelay, function()
                indicator.Visible = false
                isFlashing = false
            end)
        end
        
        if isHit then
            triggerFlash()
        else
            task.spawn(function()
                task.wait(0.7)
                
                while currentTargetFound do
                    task.wait(0.1)
                end
                
                triggerFlash()
            end)
        end
    end
end)
